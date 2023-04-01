# HPC Seminar Thesis Template
The thesis template consists of the following files:
- `seminarthesis.tex`: This is the main file of the template. Besides language options, you do not have to change anything here.
- `my_config.tex`: Title, author and other settings are set here.
- `abstract.tex`: Abstract of your thesis
- `my_chapters.tex`: All chapters are included in this file. You might want to add more entries here, preferably one file per chapter. The following chapters are predefined:
    - `introduction.tex`: Sample introduction chapter
    - `example.tex`: Helpful documentation for LaTeX beginners
    - `conclusions.tex`: Sample conclusion chapter
- `my_includes.tex`: In case you need special packages, please include them here.


## Installing a TeX Document Production System
The two most popular distributions are TeXLive and MiKTeX:
- https://www.tug.org/texlive/ (preferably for Unix environments)
- https://miktex.org/ (preferably for Windows environments)


## Running pdflatex
There are several options to run `pdflatex' and generate the seminar thesis document.

### Using a LaTeX Editor
There are many LaTeX editors available which automatically handle the build process. Some examples:
- TeXmaker (https://www.xm1math.net/texmaker/)
- TeXnicCenter (https://www.texniccenter.org/)
- TeXstudio (https://www.texstudio.org/)
- LaTeX Workshop for Visual Studio Code (https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)

### Using the Command Line
Either use `latexmk` (shipped with TeXLive and MiKTeX) with
```
latexmk -pdf seminarthesis.tex
``` 
or use the provided `Makefile` (which is a wrapper for `latexmk`)
```
make
```