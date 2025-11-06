# Personal website

This is the repository for my simple personal website.

It uses [Quarto](https://quarto.org/) and [GitHub Pages](https://pages.github.com/).


## Adding post

Simply add a new directory to the `posts` folder.
It needs to have a `index` file in it. It can be `qmd`, `jupyter`. Then you need to add at least these things to the yaml frontmatter

```yaml
---
title: "Title"
date: 'yyyy-mm-dd'
categories: ["category"]
---
```

## Previewing the site locally

Yo ucan preview this using quarto

```bash
uv run quarto preview
```

## Setting up environment

### Clone repository

This can be done with

```bash
git clone https://github.com/jamesthompson/1jamesthompson1.github.io.git
cd 1jamesthompson1.github.io
```

### Install dependencies

```bash
uv sync
```
