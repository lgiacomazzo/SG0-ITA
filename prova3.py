#1 regex files

# per ogni file che rispecchiano il regex
# aggiungo ogni linea a una dict
# key: frase, value: contatore
# salva tutto il dict su un file txt
# poi leggo con excel e ordino


import sys
import pathlib
import re
from collections import defaultdict

regex_expr = sys.argv[1]
mappa = dict()
for path in pathlib.Path(".").glob(regex_expr):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            frase_corretta = line.strip()
            line_2 = re.split("^(\[name\].*\[line\])", frase_corretta)
            if len(line_2) == 1:
                continue
            # line_2 = ['', '[name].*[line]', 'resto stringa'] or ['', '', line_1]
            mappa[line_2[1]] = 1

with open("risultato_analisi_files.txt", "w", encoding="utf-8") as file:
    for frase,contatore in mappa.items():
        stringa_da_salvare = frase
        print(stringa_da_salvare, file=file, end='\n')

