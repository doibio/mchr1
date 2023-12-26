all: thesis.pdf

clean:
	rm -f *toc *aux *out *log *bbl *blg

thesis.pdf: clean thesis.tex frontmatter/* thesis.bib
	/usr/bin/pdflatex -file-line-error -halt-on-error thesis.tex && bibtex thesis && /usr/bin/pdflatex -file-line-error -halt-on-error thesis.tex && /usr/bin/pdflatex -file-line-error -halt-on-error thesis.tex
