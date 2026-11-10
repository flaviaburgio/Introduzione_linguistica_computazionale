from urllib import request

#esercizio 1
def leggi_dati(url):
    risultato=[]
    chiavi=[]
    with request.urlopen(url) as oggetto:
        for pos, riga in enumerate(oggetto):
            if pos==0:
                chiavi=riga.strip().decode().split(",")
                for posC, chiave in enumerate (chiavi):
                    chiavi[posC]= chiave.strip()
            else:
                valori=riga.strip().decode().split(",")
                diz={}
                for posV, valore in enumerate (valori):
                    valori[posV]=valore.replace('"','').strip()
                    if chiavi[posV] in ["Anno", "ID"]:
                        valori[posV]= int(valori[posV])
                    diz.update({chiavi[posV]: valori[posV]})
                risultato.append(diz)
        return risultato

url="https://pastebin.com/raw/pNEu1V0K"
lista_diz= leggi_dati(url)
print(lista_diz)

#esercizio 2
def filtra_ID (lista:list)-> list:
    risultato=[]
    for diz in lista:
        if diz["Città"] == "Parigi":
            risultato.append(diz["ID"])
    return risultato

opere_Parigi=filtra_ID(lista_diz)

#esercizio 3
def filtra_titoli (nome:str, lista:list)-> list:
    risultato=[]
    for diz in lista:
        if nome in diz["Titolo"]:
            risultato.append(diz["Titolo"])
    return risultato

titoli_filtrati=filtra_titoli("La", lista_diz)

#esercizio 4
def opere_per_citta (lista:list) -> list:
    risultato=[]
    lista_citta=[]
    for diz in lista: #seleziono città e la appendo alla lista delle città.
        citta= diz["Città"]
        if citta not in lista_citta:
            lista_citta.append(citta)

    for elemento in lista_citta: #per ogni città creo una lista
        lista_opere=[]  #per inserire le opere devo iterare sui dizionari
        for diz in lista:
            if diz["Città"] == elemento:
                lista_opere.append(diz["Titolo"])
        tupla= (elemento, lista_opere)
        risultato.append(tupla)
    return risultato

tuple_citta_opere=opere_per_citta(lista_diz)

#esercizio 5
def salva_su_file(lista:list,nome:str):
    with open(nome,"w", encoding="utf-8") as file:
        for tupla in lista:
            file.write(f"{tupla[0]}: ")
            titoli= tupla[1]
            for pos, titolo in enumerate (titoli):
                file.write(f"{titolo}")

                if pos < len(titoli)-1:
                    file.write(", ")
                else:
                    file.write(";\n")

salva_su_file(tuple_citta_opere, "città e opere.txt")

