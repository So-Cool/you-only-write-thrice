#! /usr/bin/env bash

IN=src/text
OUT=_build/html/slides

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

build_exec_deck bayesian_networks-mnb.md
build_exec_deck bayesian_networks-jnb.ipynb
build_exec_deck bayesian_networks-pnb.py
