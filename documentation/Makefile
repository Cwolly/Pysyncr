TEXFILES=requirements.tex
PDFFILES=$(subst tex,pdf,$(TEXFILES))
JUNK=$(subst pdf,aux,$(PDFFILES)) $(subst pdf,log,$(PDFFILES))

.PHONY: all
all: $(PDFFILES)

%.pdf: %.tex
	pdflatex $<
	pdflatex $<
	pdflatex $<
	rm $(JUNK)

clean:
	rm $(PDFFILES)
