# 1
def stringhe_con_due_a (L:list) -> list:
    risultato = []
    for stringa in L:
        if stringa [3:10].count("a")>=2:  #se nei caratteri della stringa dalla pos 3 a 9 si contano almeno 2 "a"
            risultato.append(stringa)
    return risultato
#count() è un metodo di stringhe, tuple e liste!!

lista= ["xxxaxxxaxa", "xxxxxaxxxa", "xxxxxxxxxx", "xxxaaaaaaa", "bbbbbbbbbbbb"]
print(stringhe_con_due_a(lista))

# 2
def primo_e_ultimo_carattere(lista:list) -> str:
    risultato = ""
    for stringa in lista:
        risultato += stringa [0] + stringa[len(stringa)-1]
    return risultato

lista= ["cxxxi", "axxxo"]
print(primo_e_ultimo_carattere(lista))  #ciao

# 3
def inverti_ordine_parole (lista:list) -> str:
    risultato = ""
    for pos in range (len(lista)-1, -1, -1):  #da pos 1 a 0 indietro
        risultato = risultato + lista[pos] #al primo ciclo aggiungo la stringa in ultima posizione.
    return risultato

lista= ["ciao ", "mondo "]
print(inverti_ordine_parole(lista))

# più semplice:
def inverti_ordine_parole (lista:list) -> str:
    risultato = ""
    lista[0], lista[1]= lista[1], lista[0]
    for stringa in lista:
        risultato = risultato +  stringa
    return risultato

lista= ["ciao ", "mondo "]
print (inverti_ordine_parole(lista))

# 4
def operazione (lista1:list, lista2:list):
    risultato = ""
    for pos in range (0,len(lista1)): #devo generare le posizioni
        risultato+= lista1[pos] +lista2[pos]
    return risultato

lista1 = ['a', 'b', 'c']
lista2 = ['1', '2', '3']
print (operazione (lista1, lista2))

# 5
def funzione (lista1:list, lista2:list)-> str:
    risultato= ""
    pos = 0
# PRIMO WHILE - Alterna finché ci sono elementi in ENTRAMBE
# Questo ciclo continua finché pos è minore di entrambe le lunghezze.
# Alterna caratteri finché entrambe le liste hanno ancora elementi

    while pos < len(lista1) and pos < len(lista2):
        risultato= risultato + lista1[pos] +lista2[pos]
        pos += 1

#SECONDO WHILE - Aggiunge ciò che resta di lista2
# Se lista2 è più lunga, aggiunge i suoi caratteri rimanenti
    while pos < len(lista2):
        risultato= risultato + lista2[pos]
        pos += 1

# TERZO WHILE - Aggiunge ciò che resta di lista1
# Se lista1 è più lunga, aggiunge i suoi caratteri rimanenti
    while pos < len(lista1):
        risultato= risultato + lista1[pos]
        pos += 1

    return risultato
lista1=['a', 'b', 'c', 'd', 'e'] #lunghezza 5
lista2=['1', '2', '3']  #lunghezza 3
print (funzione(lista1, lista2))

# 6
def conta_voc_cons (stringa:str) -> str:
    vocali= "aeiouAEIOU"
    conteggio_voc=0
    conteggio_con=0
    for car in stringa:
        if car in vocali:
            conteggio_voc+=1
        else:  #sarà una consonante dato che sono ammessi solo questi caratteri!!
            conteggio_con+=1
    if conteggio_voc > conteggio_con:
        return "più vocali"
    elif conteggio_con > conteggio_voc:
        return "più consonanti"
    else:
        return "uguale numero di vocali e consonanti"

stringa= "mamma"
risultato= conta_voc_cons(stringa)
print(risultato)

# 7
def conta_vocali_consonanti (stringa:str) -> str:
    vocali= "aeiouAEIOU"
    consonanti = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    numero_voc=0
    numero_cons=0
    for car in stringa:
        if car in vocali:
            numero_voc+=1
        elif car in consonanti:
            numero_cons+=1
    if numero_voc > numero_cons:
        return "più vocali"
    elif numero_cons > numero_voc:
        return "più consonanti"
    else:
        return "uguale numero di vocali e consonanti"

stringa= "mamma25654aaaaaaaaaaaaaaaa"
print(conta_vocali_consonanti(stringa))

# 8
def filtra_elementi (lista1:list, lista2:list) -> list:
    risultato= []
    # non possiamo usare "remove()" perchè toglie solo la prima occorrenza.
    # Quindi invece di togliere dalla prima lista, dobbiamo creare una nuova lista di soli elementi diversi.

    for elemento in lista1:
        if elemento not in lista2:
            risultato.append(elemento)

    return risultato

lista1= ["ciao","flavia", "sole", "mare"]
lista2= ["ciao", "flavia", "come", "stai"]
print(filtra_elementi(lista1, lista2))

