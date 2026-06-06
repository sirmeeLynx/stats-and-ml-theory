.PHONY: all notes latex pdf clean

all: notes

notes: latex pdf

latex:
	@mkdir -p generated
	@for file in obsidian/*.md; do \
		name=$$(basename "$$file" .md | tr ' ' '-'); \
		pandoc "$$file" \
			--from markdown+wikilinks_title_after_pipe+tex_math_dollars+tex_math_single_backslash \
			--to latex \
			-o "generated/$$name.tex"; \
	done

pdf:
	@mkdir -p build
	@(printf '%s\0' obsidian/index.md; find obsidian -maxdepth 1 -name '*.md' ! -name 'index.md' -print0 | sort -z) | \
		xargs -0 pandoc \
			--from markdown+wikilinks_title_after_pipe+tex_math_dollars+tex_math_single_backslash \
			--pdf-engine=tectonic \
			-o build/stats-and-ml-theory.pdf

clean:
	rm -rf build generated
