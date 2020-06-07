#!/usr/bin/env sh

echo $1
cd $(dirname $1)
echo $PWD
nom="$(basename $1 .tex)"
echo ${nom}

sed -e 's/VersionDocument}{\[0-9]}/VersionDocument}{1}/' "${nom}.tex" > "${nom}-Prof.tex"
latexmk -C -pdf -silent -synctex=1 "${nom}-Prof.tex"
sed -e 's/VersionDocument}{\[0-9]}/VersionDocument}{2}/' "${nom}.tex" > "${nom}-Eleve.tex"
latexmk -C -pdf -silent -synctex=1 "${nom}-Eleve.tex"
sed -e 's/VersionDocument}{\[0-9]}/VersionDocument}{3}/' "${nom}.tex" > "${nom}-Public.tex"
latexmk -C -pdf -silent -synctex=1 "${nom}-Public.tex"

rm ${nom}-Prof.tex
rm ${nom}-Eleve.tex
rm ${nom}-Public.tex
