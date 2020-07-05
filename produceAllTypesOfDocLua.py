#!/usr/bin/env python3
import tempfile
import os
import sys
import shutil
from subprocess import run

def baseDuNom(nom):
    return os.path.basename(nom).split('.')[0]

def extension(nom):
    return os.path.basename(nom).split('.')[-1]

def repertoire(nom):
    return os.path.dirname(nom)

def asciiAlone(string):
    string = string.replace("à","a")
    string = string.replace("ç","c")
    string = string.replace("é","e")
    string = string.replace("è","e")
    string = string.replace("ê","e")
    string = string.replace("ë","e")
    string = string.replace("ï","i")
    string = string.replace("ô","o")
    string = string.replace("ö","o")
    string = string.replace("ù","u")
    string = string.replace(" ","_")
    return string

if __name__ == "__main__":
    # execute only if run as a script
    nom = sys.argv[1].strip("\"")
    base = baseDuNom(nom)
    print(nom)
    print(base)
    print(os.getcwd())

# à changer si l'on souhaite changer autre chose
optionAFaireEvoluer = "\\UPSTIidVersionDocument"
valeursAPrendre = [str(i) for i in range(1,4)]
extensions = ["-Prof", "-Eleves", "-Public"]

fichier = open(nom, encoding="utf-8")
corps = fichier.read()
fichier.close()

# on crée un dossier temporaire pour la compilation
tmpDir = tempfile.mkdtemp()
# on copie les sous-dossiers dans le dossier temporaire
# pour avoir accès aux sources des images
for subDir in next(os.walk('.'))[1]:
    shutil.copytree(subDir, tmpDir + "/" + subDir)

d = corps.find(optionAFaireEvoluer)

if d != -1:
    print(tmpDir)
    d = d + corps[d:].find("{")
    f = corps[d:].find("}")
    # corps[(d+1):(d+f)]
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
            run("lualatex -synctex=1 -interaction=nonstopmode --shell-escape \""+newTex+"\"",
                cwd=tmpDir,
                shell=True)
        pathNewPdf = tmpDir + "/" + base + ext + ".pdf"
        pathDestPdf = os.getcwd() + "/" + base + ext + ".pdf"
        shutil.copyfile(pathNewPdf, pathDestPdf)
    shutil.rmtree(tmpDir)
else:
    print("Option à faire évoluer non-trouvé")
