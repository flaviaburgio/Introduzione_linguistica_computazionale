from urllib import request

#esercizio 1
def leggi_file(url:str)->list:
    risultato=[]
    with request.urlopen(url) as oggetto:
        for pos, riga in enumerate(oggetto):
            if pos == 0:
                colonne= riga.strip().decode().split(",")
            else:
                righe= riga.strip().decode().split(",")
                sottolista=[] #per ogni riga

                for posR, elemento in enumerate(righe):
                    tupla=(pos, colonne[posR], elemento)
                    sottolista.append(tupla)  #per ogni elemento
                risultato.append(sottolista)
        return risultato
lista_liste=leggi_file("https://pastebin.com/raw/tnLxFxJs")

#esercizio 2
def ottieni_developer(lista:list)-> list:
    lista_dev=[]
    for sottolista in lista:
        developer=sottolista[2][2]
        if developer not in lista_dev:
            lista_dev.append(developer)
    return lista_dev

lista_developer=ottieni_developer(lista_liste)

#esercizio 3
def get_videogiochi_dopo_2017 (lista:list)-> list:
    risultato=[]
    for sottolista in lista:
        anno= int(sottolista[1][2])
        if anno > 2007:
            risultato.append(sottolista[0][2])
    return risultato

videogiochi_dopo_2017=get_videogiochi_dopo_2017(lista_liste)

#esercizio 4
def filtra_costoTot_superiore (lista:list)-> list:
    risultato=[]
    for sottolista in lista:
        costoTot= int(sottolista[4][2])
        costoDev= int(sottolista[5][2])
        if costoTot > costoDev:
            risultato.append(sottolista[0][2])
    return risultato

giochi_costoTot_superiore= filtra_costoTot_superiore(lista_liste)

#esercizio 5
def salva_su_file(ese2,ese3,ese4,nome= "output.txt"):
    with open(nome, "w", encoding="utf-8") as file:
        file.write(f"{ese2}\n{ese3}\n{ese4}\n")

risultati= (lista_developer,videogiochi_dopo_2017,giochi_costoTot_superiore)
salva_su_file(*risultati)