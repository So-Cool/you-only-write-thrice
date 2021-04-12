#! /usr/bin/env bash

IN=src/text
OUT=_build/html/notebooks

mkdir -p $OUT

purge_notebook () {
  if [[ $1 == *.ipynb ]]; then
    # Purge notebook
    jupyter nbconvert $IN/$1 \
      --TagRemovePreprocessor.remove_cell_tags='{"purge-cell"}' \
      --output-dir=$OUT
  else
    # Replace current extension with .ipynb
    fname=${1%.*}.ipynb
    # Convert current notebook format into Jupyter Notebook
    jupytext --to notebook --output $OUT/$fname $IN/$1
    # Purge notebook
    jupyter nbconvert $OUT/$fname \
      --TagRemovePreprocessor.remove_cell_tags='{"purge-cell"}' \
      --inplace
  fi
}
