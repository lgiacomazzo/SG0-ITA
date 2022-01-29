path_dir = "SG0-2.1.1/immagini_c0data"
print("")
print("")
print(f"cd {path_dir}")
lista_png = ["BG12A.png","BG24A1.png","BG24A3.png","BG24A4.png","BG24A5.png","BG24E1.png","BG24E4.png","BG24N1.png","BG24N3.png","BG24N4.png","BG83A3.png","IBG094.png","IBG099.png","SG0_IBG004A.png","SG0_IBG005A.png","SG0_IBG005C.png","SG0_IBG010A.png","SG0_IBG010B.png","SG0_IBG015A.png","SG0_IBG019A.png","SG0_IBG031A.png","SG0_IBG031B.png","SG0_IBG031C.png","SG0_IBG031D.png","SG0_IBG031E.png","SG0_IBG031F.png","SG0_IBG031G.png","SG0_IBG034A.png","SG0_IBG034B.png","SG0_IBG034C.png","SG0_IBG035A.png","SG0_IBG048A.png","SG0_IBG049A_honorifics.png","SG0_IBG049B_honorifics.png","SG0_IBG052A.png","SG0_IBG056C.png","SG0_IBG058A.png","z_warning.png"]
lista_dds = ["CLEARLIST.dds","CONFIG.dds","DATA01.dds","EXMENU.dds","EXMENU2.dds","GSYSMES.dds","help00.dds","help01.dds","MENUCHIP.dds","MESWIN.dds","PHONE.dds","PHONE_B.dds","PHONE_RINE.dds","SAVEMENU.dds","SYSM_SAVEMENU.dds","SYSM_TIPS.dds","TIPSCHIPS.dds","title_chip.dds"]
#pipeline = ["replace", "add"]
pipeline = ["replace"]

for nome in lista_png:
        for op in pipeline:
            print("open c0data.mpk")
            print(f"{op} {nome}")
            print("close c0data.mpk")

for nome in lista_dds:
        for op in pipeline:
            print("open c0data.mpk")
            print(f"{op} {nome}")
            print("close c0data.mpk")         
print("exit")
print("")
print("")
print(f"copia questi comandi nella shell di Ungelify, ma prima, copia il file c0data.mpk nella directory {path_dir}")