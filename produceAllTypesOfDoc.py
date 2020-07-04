#!/usr/bin/env python3
import tempfile
import os
import sys
import shutil
from subprocess import run

nom = "/home/kovaltct/Git/LatexMultiOS/testAndEnjoy.tex"

if __name__ == "__main__":
    # execute only if run as a script
    nom = sys.argv[1]
    print(nom)
    print(os.getcwd())

def baseDuNom(nom):
    return os.path.basename(nom).split('.')[0]

def extension(nom):
    return os.path.basename(nom).split('.')[-1]

def repertoire(nom):
    return os.path.dirname(nom)

optionAFaireEvoluer = "\\UPSTIidVersionDocument"
valeursAPrendre = [str(i) for i in range(1,4)]
extensions = ["-Eleves", "-Prof", "-Public"]

file = open(nom)
corps = file.read()
file.close()

d = corps.find(optionAFaireEvoluer)

if d != -1:
    tmpDir = tempfile.mkdtemp()
    print(tmpDir)
    d = d + corps[d:].find("{")
    f = corps[d:].find("}")
    # corps[(d+1):(d+f)]
    base = baseDuNom(nom)
    for val, ext in zip(valeursAPrendre, extensions):
        NewCorps =  corps[:(d+1)] + \
                    val + \
                    corps[(d+f):]
        newTex = base + ext + ".tex"
        pathNewTex = tmpDir + "/" + newTex
        file = open( pathNewTex, "w")
        file.write(NewCorps)
        file.close()
        for i in range(3):
            run("pdflatex -synctex=1 -interaction=nonstopmode "+newTex,
                cwd=tmpDir,
                shell=True)
        pathNewPdf = tmpDir + "/" + base + ext + ".pdf"
        pathDestPdf = os.getcwd() + "/" + base + ext + ".pdf"
        shutil.copyfile(pathNewPdf, pathDestPdf)
    shutil.rmtree(tmpDir)
else:
    print("Option à faire évoluer non-trouvé")
