all: thesis.pdf

clean:
	rm -f *toc *aux *out *log *bbl *blg

thesis.pdf: clean thesis.tex frontmatter/* thesis.bib
	/Library/TeX/texbin/pdflatex -file-line-error -halt-on-error thesis.tex && /Library/TeX/texbin/bibtex thesis && /Library/TeX/texbin/pdflatex -file-line-error -halt-on-error thesis.tex && /Library/TeX/texbin/pdflatex -file-line-error -halt-on-error thesis.tex
