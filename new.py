#!/usr/bin/env python3
"""Create a new Quarto post skeleton under posts/<slug>/index.qmd.

Usage examples:
  uv run python scripts/new_post.py create "My Post Title"
  uv run python scripts/new_post.py create "My Post Title" --slug my-post --category notes

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


def create_post(title: str, slug: str | None, category: str | None, date: str | None, force: bool) -> str:
    if not slug:
        slug = slugify(title)
        if not slug:
            raise SystemExit("Unable to create a slug from the title; please pass --slug")
    posts_dir = os.path.join(os.getcwd(), "posts")
    post_dir = os.path.join(posts_dir, slug)
    os.makedirs(post_dir, exist_ok=True)
    index_path = os.path.join(post_dir, "index.qmd")
    if os.path.exists(index_path) and not force:
        raise SystemExit(f"Refusing to overwrite existing post: {index_path} (use --force to overwrite)")
    if not date:
        date = datetime.date.today().isoformat()

    # Format categories
    categories = category.lower().split(",") if category else []
    content = TEMPLATE.substitute(title=title.replace('"', '\\"'), date=date, categories=categories)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    return index_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="new_post.py", description="Create a new post skeleton for this Quarto site")
    parser.add_argument("title", help="Post title (quoted) ")
    parser.add_argument("--slug", help="Optional slug (folder name). If omitted, generated from title")
    parser.add_argument("--category", help="Category or comma-separated categories", default="")
    parser.add_argument("--date", help="Date (YYYY-MM-DD). Defaults to today", default=None)
    parser.add_argument("--force", help="Overwrite existing post if present", action="store_true")

    args = parser.parse_args(argv)
    try:
        path = create_post(args.title, args.slug, args.category, args.date, args.force)
    except SystemExit as e:
        print(e, file=sys.stderr)
        return 2
    print(f"Created post: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
