#!/usr/bin/env python3
"""Emit the notes in conceptual (topological) order for the PDF build.

The order is driven by the curated wiki-link sequence in ``notes/index.md`` so
the compiled PDF reads in dependency order (foundations -> distributions ->
sampling -> hypothesis testing -> ML) instead of alphabetical filename order.

Output: NUL-separated repo-relative paths, ``notes/index.md`` first, then the
notes in index order, then any note not referenced by the index appended in
sorted order (so a newly added note is never silently dropped from the PDF).
Intended to be piped into ``xargs -0 pandoc``.
"""
import glob
import os
import re
import sys

NOTES_DIR = "notes"
INDEX = os.path.join(NOTES_DIR, "index.md")


def norm(title: str) -> str:
    """Normalise a wiki-link title / filename stem to a comparable key."""
    return title.strip().lower().replace("&", "and").replace(" ", "-")


def h1_title(path):
    """Return the note's first level-1 heading text, or None."""
    for line in open(path, encoding="utf-8"):
        m = re.match(r"#\s+(.+?)\s*$", line)
        if m:
            return m.group(1)
    return None


def main() -> int:
    index_text = open(INDEX, encoding="utf-8").read()
    # Ordered wiki-link targets, dropping any "|alias" display text.
    linked = [m.split("|")[0].strip()
              for m in re.findall(r"\[\[([^\]]+)\]\]", index_text)]

    files = {f for f in glob.glob(os.path.join(NOTES_DIR, "*.md"))
             if os.path.basename(f) != "index.md"}
    by_key = {norm(os.path.splitext(os.path.basename(f))[0]): f for f in files}
    by_base = {os.path.splitext(os.path.basename(f))[0]: f for f in files}
    # Foam also resolves a wiki-link by the note's H1 title, not just its
    # filename (these can differ when filenames are short slugs).
    by_title = {}
    for f in files:
        title = h1_title(f)
        if title:
            by_title.setdefault(norm(title), f)

    ordered, used = [], set()
    for title in linked:
        path = (by_base.get(title)
                or by_key.get(norm(title))
                or by_title.get(norm(title)))
        if path and path not in used:
            ordered.append(path)
            used.add(path)
        elif not path:
            print(f"note-order: WARNING unresolved index link [[{title}]]",
                  file=sys.stderr)

    # Append any on-disk note the index does not reference, sorted, so it is
    # still included in the PDF rather than dropped.
    for path in sorted(files - used):
        print(f"note-order: WARNING note not in index, appending: {path}",
              file=sys.stderr)
        ordered.append(path)

    out = [INDEX] + ordered
    sys.stdout.write("\0".join(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
