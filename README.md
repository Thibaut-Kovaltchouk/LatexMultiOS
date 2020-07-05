# LatexMultiOS
Solution souple et pouvant être adapté assez facilement pour pouvoir compiler des documents en plusieurs version simplement et valable pour les principaux systèmes d'exploitation (à condition d'avoir Python 3.x d'installé).

Un*x correspond à la fois à Mac et Linux dans la suite (système unix-like).

## Kit de démarrage UPSTI

Récupération à l'adresse suivante :
http://s2i.pinault-bigeard.com/ressources/latex/70-kit-de-demarrage-latex-pour-les-sciences-de-l-ingenieur-upsti

Pour installer des bibliothèques sous mactex ou texlive (système un*x), il faut les mettre dans un dossier texmf local (variable TEXMFHOME) puis, une fois les sty installé correctement, il faut lancer la commande `texhash`.

## Si ce n'est pas déjà fait, installez Python 3 sur votre système

Vérifiez que python3 est bien défini sur votre système (avant l'installation si vous n'êtes pas sûr, après un redémarrage si vous avez installé Python 3) : 
* sous Windows : lancez une invite de commande (`cmd`) et tapez python3 puis entrée : normalement, cela devrait vous informer si l'installation s'est bien passé ou pas).
* sous Un*x : lancez un terminal (Terminal, xterm, qterminal,...) et faire la même chose que sous Windows.

## Télécharger le script python produceAllTypesOfDoc.py

L'installer dans un endroit qui vous convient, changez son nom si vous le souhaitez. 

## Définir une compilation personnalisée sur votre éditeur

Sous TeXstudio et sur Texmaker par exemple, vous pouvez définir une compilation personnelle :
* sous Windows, mettez la commande : `python3 "C:\Users\thiba\Documents\Git\LatexMultiOS\produceAllTypesOfDoc.py" \"%.tex\"`
* sous Un*x, mettez la commande : `"/home/kovaltct/Git/LatexMultiOS/produceAllTypesOfDoc.py" \"%.tex\"`

Vous adaptez la première partie de la commande à l'endroit où vous avez décidé de placer le script.
