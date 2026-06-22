# Stats and ML Theory

Personal notes on statistics, probability, machine learning foundations, and data science theory.

The repository is Markdown-first:

```text
Obsidian/Foam Markdown notes -> generated LaTeX -> generated PDF
```

Markdown notes are the source of truth because they support fast note-taking, wiki-links, backlinks, and graph visualization. LaTeX and PDF outputs are generated artifacts for polished reading.

## Structure

- `notes/` - source notes using Markdown and `[[wikilinks]]`
- `.foam/` - Foam graph configuration for VS Code
- `figures/` - diagrams and generated images
- `generated/` - generated LaTeX output, ignored by Git
- `build/` - generated PDF output, ignored by Git
- `src/` - helper scripts or examples

## Build

Generate LaTeX and PDF outputs:

```bash
make notes
```

Clean generated outputs:

```bash
make clean
```
