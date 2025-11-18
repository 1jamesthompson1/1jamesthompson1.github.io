#!/usr/bin/env python3
"""Create a new Quarto post skeleton under posts/<slug>/index.qmd.

Usage examples:
    uv run python scripts/new_post.py create "My Post Title"
    uv run python scripts/new_post.py create "My Post Title" --slug my-post -c notes
    uv run python scripts/new_post.py create "My Post Title" -c notes -c personal
    uv run python scripts/new_post.py create "My Post Title" -c notes,personal

This script is deliberately standalone and requires only Python stdlib so you
can run it via `uv run python ...` without installing extra packages.
"""
import argparse
import datetime
from string import Template
import os
import re
import sys

TEMPLATE = Template("""---
title: "${title}"
date: ${date}
categories: ${categories}
---


Write your post here.
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


def create_post(title: str, slug: str, categories: list[str] | None, date: str | None, force: bool) -> str:
    
    posts_dir = os.path.join(os.getcwd(), "posts")
    post_dir = os.path.join(posts_dir, slug)
    os.makedirs(post_dir, exist_ok=True)
    index_path = os.path.join(post_dir, "index.qmd")
    if os.path.exists(index_path) and not force:
        raise SystemExit(f"Refusing to overwrite existing post: {index_path} (use --force to overwrite)")
    if not date:
        date = datetime.date.today().isoformat()

    # Format categories - already a list of strings by the caller
    categories = [c.strip().lower() for c in (categories or []) if c and c.strip()]
    # Format categories as a YAML-friendly list; Quarto accepts both single value
    # or list like: categories: ['personal', 'notes']
    if not categories:
        categories_value = '[]'
    elif len(categories) == 1:
        # Keep as a YAML list with a single element
        safe = categories[0].replace("'", "''")
        categories_value = f"['{safe}']"
    else:
        safe_elems = [f"'{c.replace("'", "''")}'" for c in categories]
        categories_value = f"[{', '.join(safe_elems)}]"

    content = TEMPLATE.substitute(title=title.replace('"', '\\"'), date=date, categories=categories_value)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    return index_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="new_post.py", description="Create a new post skeleton for this Quarto site")
    parser.add_argument("title", help="Post title (quoted) ")
    parser.add_argument("--slug", help="Optional slug (folder name). If omitted, generated from title")
    parser.add_argument("--category", "-c", action="append",
                help=("Category or comma-separated categories. Repeat the flag for multiple values; "
                    "comma-separated values within a single flag are also supported."),
                default=[])
    parser.add_argument("--date", help="Date (YYYY-MM-DD). Defaults to today", default=None)
    parser.add_argument("--force", help="Overwrite existing post if present", action="store_true")

    args = parser.parse_args(argv)
    slug = args.slug
    if not slug:
        slug = slugify(args.title)
        if not slug:
            raise SystemExit("Unable to create a slug from the title; please pass --slug")
    
    # Create git branch name from slug
    branch_name = f"posts/{slug}"
    os.system(f"git checkout -b {branch_name}")

    # Support either: --category a --category b, or --category a,b
    # Flatten and split comma-separated categories
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


if __name__ == "__main__":
    raise SystemExit(main())
