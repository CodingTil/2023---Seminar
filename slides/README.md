# Theme for LaTeX beamer class, inspired by the official PowerPoint template

This theme is UNOFFICIAL and not approved by RWTH Aachen University!

(Created by Jonas Hahnfeld <Hahnfeld@itc.rwth-aachen.de>)

## Required files

 * `beamer*themeitc.sty`: Style files
 * `rwth_itcenter_rgb.pdf`: IT Center Logo

`rwth_itcenter_rgb.eps` has been used to create `rwth_itcenter_rgb.pdf` (see `Makefile`).
`example.tex` and `example169.tex` show the basic features of this theme.

## Usage

Copy the required files into a directory, create a document with `\documentclass{beamer}` and add `\usetheme{itc}`.
Please see `example.tex` and `example169.tex` for more details.

## Supported features

The current version supports the following elements:
 * title page (`\maketitle` or `\titlepage` in a `plain` frame)
   * four different formats supported (identical to those in the original PPT theme)
   * global meta data via `\title`, `\subtitle`, `\author`, and `\date`
   * optional: name of presenter via `\presenter` on title page
 * section and subsection pages (`\sectionpage`, `\subsectionpage`)
 * custom item font size
 * custom spacing between items, via itemsep option, globally or per frame
 * frame title, via option to `frame` environment or `\frametitle`
 * frame subtitle, via option to `frame` environment or `\framesubtitle`
 * `enumerate` and `itemize`
 * frame numbering at the left side of the footline
 * customizable text in the footline (default one contains title, author, institute and date)
   * `\footline` inside a frame sets the text for the current frame
   * from outside, it sets the global default
 * presenter notes

### How to get notes on a second screen

1. Create presentation and add `\note`s
2. Add some conditional lines to the preamble (see below)
3. Create a new tex file for the notes (see below):
4. Compile the new document and view it with [Dual-Screen PDF Viewer](http://dspdfviewer.danny-edel.de/).

Add the following lines to the preamble of your presentation's main file:
```
\ifdefined\includeNotes
  \usepackage{pgfpages}
  \setbeameroption{show notes on second screen}
\fi
```

The tex document must contain the following lines:
```
\def\includeNotes{1}

\input{presentation}
```
Don't forget to adjust the input file!
