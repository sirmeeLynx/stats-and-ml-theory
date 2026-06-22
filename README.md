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

## Sources

Notes are distilled from the course pages and the three live virtual classes (LVC 1–3).
Each note's YAML frontmatter records its `sources` (course page IDs and, where relevant,
the `live_class` summary/transcript IDs and recording timestamps) — this metadata feeds
the knowledge graph but does not render into the PDF. Raw LVC transcripts (WEBVTT) and
post-session summary PDFs are cached outside the repo at `~/lms/machine-learning/`.

## Build

Generate LaTeX and PDF outputs:

```bash
make notes
```

Clean generated outputs:

```bash
make clean
```
