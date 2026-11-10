from urllib import request

def leggi_dati(url:str)->list:
    risultato= []
    with request.urlopen(url) as oggetto:
        for pos, riga in enumerate(oggetto):
            if pos == 0:
                intestazione= riga.strip().decode().split(",")
            else:
                nuova_lista=[]
                righe= riga.strip().decode().split(",")
                for pos_r, elemento in enumerate(righe):
                    tripla= (pos_r, intestazione[pos_r], elemento)
                    nuova_lista.append(tripla)
                risultato.append(nuova_lista)
        return risultato


# 2
def filtra_opere_dopo_1960 (lista:list)->list:
    risultato = []
    for sottolista in lista:
        data = sottolista[2]
        anno = data[2]
        if "-" in anno:
            lista_anno = anno.split("-")
            anno = int(lista_anno[1])
        elif anno.endswith("s"):
            anno = int(anno[:len(anno) - 1])  # 1960s pos4 len5
        else:
            anno = int(anno)
        if anno > 1960:
            risultato.append(sottolista[0][2])
    return risultato


#esercizio 3
def filtra_autore_sconosciuto(lista:list)-> list:
    risultato=[]
    for sottolista in lista:
        autore= sottolista[1][2]
        if autore == "":
            libro= sottolista[0][2]
            risultato.append(libro)
    return risultato

# esercizio 4
def filtra_autore(lista:list)-> list:
    risultato=[]
    for sottolista in lista:
        guadagno_copie= sottolista[4][2]
        if guadagno_copie.endswith("s"):
            guadagno_copie= int(guadagno_copie[:len(guadagno_copie)-1])
        elif "." in guadagno_copie:
            guadagno_copie= guadagno_copie.split(".")
            guadagno_copie= int(guadagno_copie[0])
        else:
            guadagno_copie= int(guadagno_copie)

        if guadagno_copie > 1000000 and sottolista[1][2] != "":
            autore= sottolista[1][2]
            autore= autore.strip().replace('"', "") #pulisco le stringhe
            risultato.append(autore)
    return risultato

filtra_autore(lista_liste)

#esercizio 5
def salva_su_file(lista:list, nome:str):
    with open(nome,"w", encoding= "utf-8") as file:
        for sottolista in lista:
            file.write(f"{riga}\n")

salva_su_file(lista_liste, "nome file.txt")




