#! /usr/bin/env bash

IN=src/slides
OUT=_build/html/src/slides

mkdir -p $OUT

build_deck () {
  if [[ $1 == *.ipynb ]]; then
    # Convert it to slides
    jupyter nbconvert $IN/$1 --to slides --output-dir=$OUT
  else
    # Replace current extension with .ipynb
    fname=${1%.*}.ipynb
    # Convert current notebook format into Jupyter Notebook
    jupytext --to notebook --output $OUT/$fname $IN/$1
    # Convert it to slides
    jupyter nbconvert $OUT/$fname --to slides --output-dir=$OUT
    # Remove the notebook
    rm $OUT/$fname
  fi
}

build_exec_deck () {
  if [[ $1 == *.ipynb ]]; then
    # Make a copy
    cp $IN/$1 $OUT/
    fname=$1
  else
    # Replace current extension with .ipynb
    fname=${1%.*}.ipynb
    # Convert current notebook format into Jupyter Notebook
    jupytext --to notebook --output $OUT/$fname $IN/$1
  fi

  # Execute it in-place
  jupyter nbconvert --execute --inplace $OUT/$fname
  # Convert it to slides
  jupyter nbconvert $OUT/$fname --to slides --output-dir=$OUT
  # Remove the notebook
  rm $OUT/$fname
}

# poster
mkdir -p _build/html/src/poster
cp src/poster/yowt_poster.pdf _build/html/src/poster/

# slides
mkdir -p _build/html/src/img/slides
cp -r src/img/slides _build/html/src/img/
mkdir -p _build/html/_sources/src/slides
cp src/slides/yowt_slides.css _build/html/_sources/src/slides/
cp src/slides/yowt_slides.css _build/html/src/slides/custom.css
build_exec_deck yowt_slides.md
