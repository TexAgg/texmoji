TEXFILE=texmoji

.PHONY: all
all: $(TEXFILE).pdf data/emojis.json

data/emojis.json: populate.py modules/*
	python populate.py

$(TEXFILE).tex: templates/$(TEXFILE).template.tex templates/$(TEXFILE).template.sty data/emojis.json
	python main.py

$(TEXFILE).pdf: $(TEXFILE).tex $(TEXFILE).sty
	pdflatex $(TEXFILE).tex
	pdflatex $(TEXFILE).tex

.PHONY: clean
clean:
	rm -rf *.aux *.log *.out *.toc

.PHONY: view
view: $(TEXFILE).pdf
	evince $(TEXFILE).pdf