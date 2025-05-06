LATEX = pdflatex --shell-escape

SRC = ${wildcard src/*.tex src/**/*.tex}

all: main.pdf

main.pdf: main.tex macros.tex $(SRC)
	$(LATEX) main
	$(LATEX) main

clean:
	$(RM)  $(PACKAGE).cls *.log *.aux *.pdf \
	*.cfg *.glo *.idx *.toc \
	*.ilg *.ind *.out *.lof \
	*.lot *.bbl *.blg *.gls *.cut *.hd \
	*.dvi *.ps *.thm *.tgz *.zip *.rpi
