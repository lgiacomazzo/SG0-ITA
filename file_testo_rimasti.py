import sys
import pathlib
from collections import defaultdict

altri_file = ["macrosys2.scx.txt", "CLRFLG.scx.txt", "_tips.scx.txt", "_system.scx.txt", "_Startup_win.scx.txt", "_phone.scx.txt"]
capitolo_0 = ["SG0_00_01.scx.txt", "SG0_00_02.scx.txt", "SG0_00_03.scx.txt", "SG0_00_04.scx.txt"]
capitolo_1 = ["SG0_01_01.scx.txt", "SG0_01_02.scx.txt", "SG0_01_03.scx.txt", "SG0_01_04.scx.txt", "SG0_01_05.scx.txt", "SG0_01_06.scx.txt", "SG0_01_07.scx.txt", "SG0_01_08.scx.txt"]
percorso_alfa = ["SG0_A01_01.scx.txt","SG0_A01_02.scx.txt","SG0_A01_03.scx.txt"]
percorso_beta = ["SG0_B01_01.scx.txt","SG0_B01_02.scx.txt","SG0_B01_03.scx.txt","SG0_B01_04.scx.txt","SG0_B01_05.scx.txt","SG0_B01_06.scx.txt","SG0_B01_07.scx.txt","SG0_B01_08.scx.txt","SG0_B01_09.scx.txt","SG0_B01_10.scx.txt","SG0_B01_11.scx.txt","SG0_B01_12.scx.txt","SG0_B01_13.scx.txt","SG0_B01_14.scx.txt","SG0_B01_15.scx.txt","SG0_B01_16.scx.txt","SG0_B01_17.scx.txt","SG0_B01_18.scx.txt","SG0_B01_19.scx.txt","SG0_B01_20.scx.txt","SG0_B01_21.scx.txt","SG0_B01_22.scx.txt","SG0_B01_23.scx.txt","SG0_B01_24.scx.txt","SG0_B01_25.scx.txt","SG0_B02_11.scx.txt","SG0_B02_12.scx.txt","SG0_B02_13.scx.txt","SG0_B02_14.scx.txt","SG0_B02_15.scx.txt","SG0_B02_16.scx.txt","SG0_B02_17.scx.txt","SG0_B02_18.scx.txt","SG0_B02_19.scx.txt","SG0_B02_20.scx.txt","SG0_B02_21.scx.txt"]
altri_capitoli = []
gia_fatti = altri_file + capitolo_0 + capitolo_1 + percorso_alfa + percorso_beta + altri_capitoli

def print_file_sopra_i_e_non_tradotti(numero, mappa):
    global gia_fatti
    print(f"File rimasti sopra i {numero}")
    for file,contatore in mappa.items():
        if contatore >= numero and file not in gia_fatti:
            print(f"{file}: {contatore}")

# trova tutti i file e conta quante righe hanno
# passare come argomento il path dove trovare i file txt (esempio: scrivere "path/*" comporta che legge tutti i file dentro path)
# senza argomenti, di default legge dentro Traduzione_ita/testi
if len(sys.argv) >= 2:
    regex_expr = sys.argv[1]
else:
    regex_expr = r".\Traduzione_ita\testi\*"
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
#print_file_sopra_i_e_non_tradotti(300, mappa)
#print_file_sopra_i_e_non_tradotti(400, mappa)
#print_file_sopra_i_e_non_tradotti(500, mappa)
#print_file_sopra_i_e_non_tradotti(600, mappa)
print(count)