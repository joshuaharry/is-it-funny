#!/bin/sh

if [ -z "$1" ]; then
  pdflatex -halt-on-error  ./paper.tex;
else
  watchexec -e tex -- "bibtex paper && pdflatex -halt-on-error  ./paper.tex"
fi
