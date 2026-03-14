# 1. Estrarre i primi 4 caratteri dalla stringa "Imparo a programmare" utilizzando lo slicing. Stampare a schermo il risultato.
stringa= "Imparo a programmare"
print (stringa [:4])  #ometto start e step

# 2.  Usare lo slicing per ottenere la parola "utile" dalla stringa "Python è utile". Stampare a schermo il risultato.
stringa= "Python è utile"
print (stringa [9:]) #si può omettere lo stop perchè è len(stringa)

# 3.  Invertire la stringa "Ciao" utilizzando lo slicing con step negativo. Stampare a schermo il risultato
stringa= "Ciao"
print (stringa [::-1])

# 4. Usare lo slicing per ottenere solo i caratteri in POSIZIONE pari dalla stringa "Python è utile". Stampare a schermo il risultato.
stringa= "Python è utile"
print (stringa [::2])

# 5. Usare lo slicing per ottenere solo i caratteri in POSIZIONE dispari da "Python è utile". Stampare a schermo il risultato
stringa= "Python è utile"
print (stringa [1::2])

# 6. Verificare se la stringa "info@example.com" TERMINA con la sottostringa "@gmail.com" e stampare "Indirizzo gmail" in caso affermativo.
stringa = "info@example.com"
if stringa.endswith("@gmail.com"):
    print ("Indirizzo gmail")
print ("Non è un indirizzo gmail")

# 7. Verificare se la stringa "Benvenuto su Python" INIZIA con "Benvenuto". Stampare a schermo il risultato.
stringa = "Benvenuto su Python"
print (stringa.startswith("Benvenuto"))

# 8. CONTARE quante volte compare la sottostringa "abc" nella stringa "abcabcabcabc". Stampare "Trovato" se c'è almeno un'occorrenza.
stringa = "abcabcabcabc"
if stringa.count ("abc") > 0:    #anche >= 1
    print ("Trovato!")


# 9. TROVARE la posizione della parola "cielo" dalla stringa "Il sole splende
# alto nel cielo". Stampare "Alla fine" se si trova a meno di 10 caratteri dalla fine, stampare "All'inizio" altrimenti.
stringa= "Il sole splende alto nel cielo"
fine= stringa [-10::]
if "cielo" in fine:
    print ("Alla fine")
else:
    print ("All'inizio")
                        # mio più elegante uwu
# git hub
s = "Il sole splende alto nel cielo"
pos = s.find("cielo")     #prima posizione di una sottostringa
if len(s) - pos < 10:     #differenza lunghezza stringa - posizione della parola per calcolare la distanza dall'inizio della parola alla fine.
  print("Alla fine")
else:
    print("All’inizio")


# 10.  Convertire in maiuscolo la stringa "Python è interessante".
# Stampare a schermo il risultato.
stringa = "Python è interessante"
print (stringa.upper())

# 11. Convertire in minuscolo la stringa "PYTHON E INTERESSANTE".Stampare a schermo il risultato
stringa= "PYTHON E INTERESSANTE"
print (stringa.lower())

# 12. Rimuovere gli spazi iniziali e finali da la stringa "Python per tutti ".
# Stampare a schermo il risultato
stringa = "  Python per tutti  "
print (stringa.strip())


# 13. Ottenere "Nome", "Cognome" ed "Eta" dalla stringa "Nome,Cognome,Età ".
# Fare attenzione agli spazi. Stampare a schermo il risultato.
stringa = "Nome,Cognome,Età "
stringa = stringa.strip ()
# print (stringa.split(","))   ottengo una lista

lista = stringa.split(",")
for x in lista:
    print (x)    #estraggo dalla lista i singoli elementi


# 14. Verificare se la stringa "Python" è composta solo da lettere oppure se da
# caratteri alfanumerici. Stampare a schermo "Solo lettere" nel primo
# caso, "Lettere e numeri" nel secondo
stringa= "Python"
if stringa.isalpha():
    print ("Solo lettere")
elif stringa.isalnum():
    print ("Lettere e numeri")


# 15. Usare f-string per formattare una stringa contenente nome, cognome,
# età, numero di matricola e numero di cellulare di uno studente.
# Stampare a schermo il risultato.
nome= "Flavia"
cognome= "Burgio"
età= 24
matricola= 724676736
cellulare= 3425006669
print (f"Nome: {nome}, cognome: {cognome}, età: {età}, matricola: {matricola}, cellulare: {cellulare}")

