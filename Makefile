NOTES := $(wildcard notes/*.tex)
PDFS := $(NOTES:notes/%.tex=build/%.pdf)

.PHONY: all notes clean

all: notes

notes: $(PDFS)

build/%.pdf: notes/%.tex
	@mkdir -p build
	tectonic --outdir build $<

clean:
	rm -rf build

