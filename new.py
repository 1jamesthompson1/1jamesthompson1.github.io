#!/usr/bin/env python3
"""Create a new Quarto post or short form skeleton.

For posts:
    uv run python new.py post "My Post Title"
    uv run python new.py post "My Post Title" --slug my-post -c notes
    uv run python new.py post "My Post Title" -c notes -c personal

For short forms:
    uv run python new.py short "My Quick Thought"
    uv run python new.py short "My Quick Thought" -c thought
    uv run python new.py short "My Quick Thought" -c thought -c ai

This script is deliberately standalone and requires only Python stdlib so you
can run it via `uv run python ...` without installing extra packages.
"""
import argparse
import datetime
from string import Template
import os
import re
import sys

POST_TEMPLATE = Template("""---
title: "${title}"
date: ${date}
categories: ${categories}
---


Write your post here.
""")

SHORT_TEMPLATE = Template("""---
title: "${title}"
date: ${date}
categories: ${categories}
---


Write your short form here (max 280 characters).
""")


def slugify(s: str) -> str:
    s = s.strip().lower()
    # replace spaces and underscores with hyphens
    s = re.sub(r"[\s_]+", "-", s)
    # remove invalid characters
    s = re.sub(r"[^a-z0-9\-]", "", s)
    # collapse multiple hyphens
    s = re.sub(r"-+", "-", s)
    return s


def format_categories(categories: list[str] | None) -> str:
    """Format categories as YAML-friendly list."""
    categories = [c.strip().lower() for c in (categories or []) if c and c.strip()]
    if not categories:
        return '[]'
    elif len(categories) == 1:
        safe = categories[0].replace("'", "''")
        return f"['{safe}']"
    else:
        safe_elems = [f"'{c.replace("'", "''")}'" for c in categories]
        return f"[{', '.join(safe_elems)}]"


def create_post(title: str, slug: str, categories: list[str] | None, date: str | None, force: bool) -> str:
    posts_dir = os.path.join(os.getcwd(), "posts")
    post_dir = os.path.join(posts_dir, slug)
    os.makedirs(post_dir, exist_ok=True)
    index_path = os.path.join(post_dir, "index.qmd")
    if os.path.exists(index_path) and not force:
        raise SystemExit(f"Refusing to overwrite existing post: {index_path} (use --force to overwrite)")
    if not date:
        date = datetime.date.today().isoformat()

    categories_value = format_categories(categories)
    content = POST_TEMPLATE.substitute(title=title.replace('"', '\\"'), date=date, categories=categories_value)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    return index_path


def create_short(title: str, categories: list[str] | None, date: str | None, force: bool) -> str:
    """Create a new short form in shorts/ directory."""
    shorts_dir = os.path.join(os.getcwd(), "shorts")
    os.makedirs(shorts_dir, exist_ok=True)
    
    # Generate filename from title
    slug = slugify(title)
    if not slug:
        raise SystemExit("Unable to create a filename from the title")
    
    short_path = os.path.join(shorts_dir, f"{slug}.qmd")
    if os.path.exists(short_path) and not force:
        raise SystemExit(f"Refusing to overwrite existing short: {short_path} (use --force to overwrite)")
    
    if not date:
        date = datetime.date.today().isoformat()
    
    categories_value = format_categories(categories)
    rendered = SHORT_TEMPLATE.substitute(
        title=title.replace('"', '\\"'),
        date=date,
        categories=categories_value
    )
    
    with open(short_path, "w", encoding="utf-8") as f:
        f.write(rendered)
    
    return short_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="new.py", description="Create a new post or short form for this Quarto site")
    subparsers = parser.add_subparsers(dest="type", help="Type to create: 'post' or 'short'")
    
    # Post subcommand
    post_parser = subparsers.add_parser("post", help="Create a new long-form post")
    post_parser.add_argument("title", help="Post title (quoted)")
    post_parser.add_argument("--slug", help="Optional slug (folder name). If omitted, generated from title")
    post_parser.add_argument("--category", "-c", action="append",
                help=("Category or comma-separated categories. Repeat the flag for multiple values; "
                    "comma-separated values within a single flag are also supported."),
                default=[])
    post_parser.add_argument("--date", help="Date (YYYY-MM-DD). Defaults to today", default=None)
    post_parser.add_argument("--force", help="Overwrite existing post if present", action="store_true")
    
    # Short subcommand
    short_parser = subparsers.add_parser("short", help="Create a new short form (max 280 characters)")
    short_parser.add_argument("title", help="Short form title (quoted)")
    short_parser.add_argument("--category", "-c", action="append",
                help="Category or comma-separated categories",
                default=[])
    short_parser.add_argument("--date", help="Date (YYYY-MM-DD). Defaults to today", default=None)
    short_parser.add_argument("--force", help="Overwrite existing short if present", action="store_true")
    
    args = parser.parse_args(argv)
    
    if args.type == "post":
        slug = args.slug
        if not slug:
            slug = slugify(args.title)
            if not slug:
                raise SystemExit("Unable to create a slug from the title; please pass --slug")
        
        # Create git branch name from slug
        branch_name = f"posts/{slug}"
        os.system(f"git checkout -b {branch_name}")
        
        # Support either: --category a --category b, or --category a,b
        raw_cats: list[str] = []
        for c in args.category:
            if c is None:
                continue
            raw_cats.extend([part.strip() for part in c.split(",") if part.strip()])
        
        try:
            path = create_post(args.title, slug, raw_cats, args.date, args.force)
        except SystemExit as e:
            print(e, file=sys.stderr)
            return 2
        print(f"Created post: {path}")
        return 0
    
    elif args.type == "short":
        # Support comma-separated categories, just like posts
        raw_cats: list[str] = []
        for c in args.category:
            if c is None:
                continue
            raw_cats.extend([part.strip() for part in c.split(",") if part.strip()])
        
        try:
            path = create_short(args.title, raw_cats, args.date, args.force)
        except SystemExit as e:
            print(e, file=sys.stderr)
            return 2
        print(f"Created short form: {path}")
        return 0
    
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
