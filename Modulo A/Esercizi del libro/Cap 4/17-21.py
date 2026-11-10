# 17. Data una stringa inserita dall'utente, stampare tutti i caratteri della stringa.
stringa= input ("Inserisci un messaggio: ")
for pos in stringa:
    print (pos)

# 18. Data una stringa inserita dall'utente, stampare tutti i caratteri in posizione pari della stringa.
stringa = input ("Inserisci un messaggio: ")
for pos in range (0, len (stringa), 2):
    print (stringa [pos])

# 19. Data una stringa inserita dall'utente, stampare tutti i caratteri in posizione dispari della stringa.
stringa = input ("Inserisci un messaggio: ")
for pos in range (1, len (stringa), 2):
    print (stringa [pos])


# 20. Data la stringa inserita dall'utente, stampare i caratteri della stringa, a due a due, saltando due caratteri.
# Ad esempio, presa la stringa messaggio, stampare in ordine me, ag, o.

stringa= input ("Inserisci un messaggio: ")
for pos in range(0, len(stringa), 4):  #MESSAGGIO
    if pos + 1 < len(stringa):
       print(stringa[pos] + stringa[pos + 1])
    else:
     print(stringa[pos])

#PIU' ELEGANTE USANDO LO SLICING!  (ludovica)
testo = input("Inserisci una stringa: ")
i = 0
while i < len(testo):
    coppia = testo[i:i+2]
    print(coppia)
    i += 4



# 21. Data una stringa inserita dall'utente, stampare tutti i caratteri a partire dall'ultimo.
stringa = input ("Inserisci un messaggio: ")
for pos in range (len (stringa) -1, -1,-1):
    print (stringa [pos])