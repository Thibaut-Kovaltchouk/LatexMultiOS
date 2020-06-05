#!/usr/bin/env sh
export PATH=$PATH:'~/.packagesLaTeX/UPSTI'
export PATH=$PATH:'~/.packagesLaTeX/Papanicola'
export PATH=$PATH:'~/.packagesLaTeX/Autres'

input=$(ls *.tex)
nom=${var%%.*}

sed -e 's/VersionDocument}{\[0-9]}/VersionDocument}{1}/' ${nom}.tex > ${nom}-Prof.tex
latexmk -C -pdf -silent -synctex=1 -p ${nom}-Prof.tex
sed -e 's/VersionDocument}{\[0-9]}/VersionDocument}{2}/' ${nom}.tex > ${nom}-Eleve.tex
latexmk -C -pdf -silent -synctex=1 -p ${nom}-Eleve.tex
sed -e 's/VersionDocument}{\[0-9]}/VersionDocument}{3}/' ${nom}.tex > ${nom}-Public.tex
latexmk -C -pdf -silent -synctex=1 -p ${nom}-Public.tex

rm ${nom}-Prof.tex
rm ${nom}-Eleve.tex
rm ${nom}-Public.tex
