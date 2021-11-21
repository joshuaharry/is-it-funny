#!/bin/sh

if [ -z "$1" ]; then
  pdflatex -halt-on-error -output-directory=out ./paper.tex;
else
  watchexec -e tex -- pdflatex -halt-on-error -output-directory=out ./paper.tex
fi
