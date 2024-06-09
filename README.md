This is the repositry for my simple personal website.

It uses [Quarto](https://quarto.org/) and [GitHub Pages](https://pages.github.com/).

# Instructions

These instrucitons are here for myself to know what is going on.

## Adding post

Simply add a new directory to the `posts` folder.
It needs to have a `index` file in it. It can be `qmd` or `jupyter`. Then you need to add atleast these things to the yaml frontmatter
```yaml
---
title: "Title"
date: 'yyyy-mm-dd'
categories: ["category"]
---
```

## Setting up environment

You need to do three things:

### [Install Quarto](https://quarto.org/docs/get-started/install.html)
Just follow the instructions. This is so that you can use the various quarto commands. The editor extension is optional.

### Clone repository
This can be done with
```bash
git clone https://github.com/jamesthompson/1jamesthompson1.github.io.git
cd 1jamesthompson1.github.io
```

### Setup pre-commit
There is a pre-commit which makes sure that the conda environment is up to date. You can do this with by adding this code to the `.git/hooks/pre-commit` file.
```
#!/bin/bash

# Export the Conda environment
conda env export --no-builds | grep -v "^prefix: " > environment.yml

# Add the updated environment.yml to the commit
git add environment.yml

# Proceed with the commit
exit 0
```






