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

gia_fatti = ["macrosys2.scx.txt", "CLRFLG.scx.txt", "_tips.scx.txt", "_system.scx.txt", "_Startup_win.scx.txt", "_phone.scx.txt","SG0_00_01.scx.txt", "SG0_00_02.scx.txt", "SG0_00_03.scx.txt", "SG0_00_04.scx.txt", "SG0_01_01.scx.txt", "SG0_01_02.scx.txt", "SG0_01_03.scx.txt", "SG0_01_04.scx.txt", "SG0_01_05.scx.txt", "SG0_01_06.scx.txt"]

def print_file_sopra_i_(numero, mappa):
    print(f"File rimasti sopra i {numero}")
    for file,contatore in mappa.items():
        if contatore >= numero:
            print(f"{file}: {contatore}")

def print_file_sopra_i_e_non_tradotti(numero, mappa):
    global gia_fatti
    print(f"File rimasti sopra i {numero}")
    for file,contatore in mappa.items():
        if contatore >= numero and file not in gia_fatti:
            print(f"{file}: {contatore}")


regex_expr = sys.argv[1]
mappa = defaultdict(lambda: 0)
for path in pathlib.Path(".").glob(regex_expr):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                mappa[path.name] += 1

# proprio tutti i file rimasti e quante righe sono
count = 0
for file,contatore in mappa.items():
    if file not in gia_fatti:
        count += contatore

print_file_sopra_i_e_non_tradotti(0, mappa)
print_file_sopra_i_e_non_tradotti(300, mappa)
print_file_sopra_i_e_non_tradotti(400, mappa)
print_file_sopra_i_e_non_tradotti(500, mappa)
print_file_sopra_i_e_non_tradotti(600, mappa)
print(count)