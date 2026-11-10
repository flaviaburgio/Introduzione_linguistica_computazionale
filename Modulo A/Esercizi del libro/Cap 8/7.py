from urllib import request

#esercizio 1
def leggi_file(url:str)-> list:
    risultato=[]
    chiavi=[]
    with request.urlopen(url) as oggetto:
        for pos, riga in enumerate(oggetto):
            if pos==0:
                chiavi= riga.strip().decode().split(",")
            else:
                valori=riga.strip().decode().split(",")
                diz = {}
                for posV, valore in enumerate(valori):
                    if posV==3:
                        valori[posV]= valore.split("-")
                    elif posV==4:
                        valori[posV]= valore.split("-")

                for posC, chiave in enumerate(chiavi):
                    diz.update({chiave:valori[posC]})
                risultato.append(diz)
        return risultato

url="https://pastebin.com/raw/b9qDVyzE"
lista_diz=leggi_file(url)


#esercizio 2
def tot_calorie (lista:list)->str:
    somma=0
    for diz in lista:
        diz["Calorie"]= int(diz["Calorie"])
        somma+=diz["Calorie"]
    return f"Il contenuto calorico del menù offerto è di {somma} kcal"

calorie_menu=tot_calorie(lista_diz)

#esercizio 3
def menu_senza_uova(lista:list)->list:
    risultato=[]
    for diz in lista:
        nuovo_diz = {}
        if "Uova" not in diz["Ingredienti Primari"] and diz["Ingredienti Secondari"]:
            for chiave in diz:
                nuovo_diz.update({chiave:diz[chiave]})
            risultato.append(nuovo_diz)
    return risultato

piatti_senza_uova= menu_senza_uova(lista_diz)

#esercizio 4
def filtra_piatti (lista:list, kcal: int|float, ingrediente_secondario:str, tempo_cottura:int|float) -> list|None:
    risultato=[]
    for diz in lista:
        diz["Tempo"]= int(diz["Tempo"])
        if diz["Calorie"] < kcal and ingrediente_secondario not in diz["Ingredienti Secondari"] and tempo_cottura < diz["Tempo"]:
            tupla= (diz["Nome"], diz["Calorie"], diz["Tempo"])
            risultato.append(tupla)
    return risultato

lista_piatti_filtrati=filtra_piatti(lista_diz, 700, "Pepe", 30)
print(lista_piatti_filtrati)

#esercizi 5
def salva_su_file (lista:list, nome):
    with open(nome, "w", encoding="utf-8" ) as file:
        for tupla in lista:
            nome=tupla[0]
            calorie= tupla[1]
            tempo= tupla[2]
            file.write(f"{nome} - {calorie} - {tempo};")

salva_su_file(lista_piatti_filtrati, "piatti filtrati.txt")
