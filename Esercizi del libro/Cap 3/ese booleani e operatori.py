#Scrivi un programma che chiede l'età e determina se la persona è maggiorenne (18+ anni).
#METODO 1
'''

''''''
risposta_utente=  int (input ("Inserisci la tua età: "))
if risposta_utente >= 18: #devo convertire in int anche l'input che di base è considerato str
    print ("Sei maggiorenne")
else:
    print ("Sei minorenne")

#METODO2
età = int(input("Inserisci la tua età: "))
è_maggiorenne = età >= 18  #produce TRUE/FALSE
print(f"Sei maggiorenne? {è_maggiorenne}") #stampa TRUE/FALSE

#Verifica se un numero è pari usando l'operatore modulo.
#METODO 1
numero = int(input("Inserisci un numero: "))
if numero%2 ==0 :
    print ("è pari")
else:
    print ("è dispari")

#METODO 2
numero = int(input("Inserisci un numero: "))
pari= numero%2 == 0  #restituisce TRUE/FALSE
print (f"Sei pari? {pari}")

#Controlla se un numero è compreso tra 10 e 20 (inclusi).
numeroscelto= int (input("Inserisci un numero: "))
compreso= numeroscelto >=10 and numeroscelto<=20  #basta che una delle condizioni sia falsa per essere falso, dunque non compreso.
print (f"E' un numero compreso tra 10 e 20? {compreso}")
'''

#Verifica se una persona può accedere a un locale (deve essere maggiorenne O avere un permesso speciale).
#METODO 1
età= int (input("Quanti anni hai? \n"))
permesso= str (input("Hai un permesso speciale (si/no)? \n")).lower () #QUI "STR" NON SERVE PERCHE' INPUT RESTITUISCE GIA UNA STRINGA!!!
if età >=18 or permesso.startswith("s"):   #avevo scritto " permesso == "si" MA COSI PRENDE DIVERSI MODI DI SCRIVERE "SI".
    print ("Accesso consentito")
else:
    print ("Accesso negato")

#METODO 2 - PIU CREATIVO
risposte_positive = {"si", "sì", "s", "yes", "y"}
età= int (input("Quanti anni hai? \n"))
permesso = input("Hai un permesso?(si/no)").lower() #SI /NO
ha_permesso=età >=18 or permesso in risposte_positive

if ha_permesso:  #TRUE
    print("OK!")
else:
    print("Negato")