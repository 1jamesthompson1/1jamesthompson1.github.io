# Personal website

This is the repository for my [simple personal website](https://james.sjhl.nz).

It uses [Quarto](https://quarto.org/) and [GitHub Pages](https://pages.github.com/).


## Adding post

```bash
uv run new.py Post "My Post Title" -c category
```
This is creathed a new post in `posts/my-post-title/index.qmd` with the appropriate front matter as well as put you on a new git branch.

## Adding short form post

```bash
uv run new.py short "My Short Form Title" -c category
```

This creates a new short form post in `shorts/my-short-form-title.qmd` with the appropriate front matter, yet *It doest not* put you on a new git branch.

## Previewing the site locally

Yo ucan preview this using quarto

```bash
uv run quarto preview
```

## Setting up environment

### Install Quarto

Follow instructions at https://quarto.org/docs/get-started/

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
