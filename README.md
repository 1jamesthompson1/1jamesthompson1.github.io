# Personal website

This is the repository for my simple personal website.

It uses [Quarto](https://quarto.org/) and [GitHub Pages](https://pages.github.com/).


## Adding post

```bash
uv run new.py "My Post Title" --categories category
```


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
