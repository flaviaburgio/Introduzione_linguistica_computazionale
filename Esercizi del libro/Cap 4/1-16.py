# 1. Stampare a schermo i numeri da 15 a 121.
for numeri in range (15, 122):
    print (numeri)

# 2. Stampare a schermo le lettere da "a" a "m"
letteree = "abcdefghijklm"
for pos in letteree:
    print (pos)

alfabeto= "abcdefghijklmnopqrstuvwxyz"
for pos in alfabeto:
    print (pos, end= " ")
    if pos == "m":
        break

alfabeto= "abcdefghijklmnopqrstuvwxyz"
for pos in range (13)  #solo lo Stop
    print (stringa[pos])

# 3. Stampare a schermo le lettere da "n" a "z"
letteree = "abcdefghijklmnopqrstuvz"
for pos in range (13, len (letteree)):
    print (letteree[pos])

# 4. Stampare a schermo i numeri pari da 2 a 20.
for numeri1 in range(2,21,2):
        print (numeri1)

# 5. Stampare a schermo i numeri dispari da 1 a 19.
for numeri4 in range(1,20,2):
    print (numeri4)

# 6. Stampare a schermo i numeri da 50 a 40 in ordine decrescente.
for i in range (50, 39, -1):
    print (i)

# 7. Stampare a schermo i quadrati dei numeri da 1 a 10.
for x in range (1, 11):
    print (x**2)

# VERSIONE CON OUTPUT PIU CHIARO
for numero in range(1, 11):
    print(f"{numero}² = {numero**2}")

# 8. Stampare a schermo il cubo dei numeri da 1 a 5.
for ciao in range (1, 6):
    print (ciao**3)

# VERSIONE CON OUTPUT PIU CHIARO
for ciao in range(1, 6):
    print(f"{ciao} alla terza = {ciao**3}")


# 9. Stampare i numeri da 1 a 100 divisibili per 10.
for numero in range (1, 101):
    if numero%10==0:
        print (numero)

#OPPURE CON STEP
for numero in range (10, 101, 10):
    print (numero)


# 10. Stampare a schermo i numeri da 1 a 20 a eccezione dei multipli di 3.
for numero in range (1, 21):
    if not numero%3 == 0:
        print (numero)


# 11. Stampare a schermo i numeri compresi tra x e y interropendo la stampa
#se il valore è z. x,y,z devono essere inseriti dall'utente.
x= int (input ("x: "))
y= int (input ("y: "))
z= int (input ("z: "))
for numero in range (x, y+1):
    print(numero)
    if numero == z:
        break



# 12. Stampare a schermo i numeri da x a y in ordine decrescente, dove x e y sono inseriti dall'utente.
x= int (input ("inserisci un numero: "))
y= int (input ("inserisci un numero: "))
if x<= y:
    print ("x deve essere maggiore di y")
    x = int(input("inserisci un numero: "))
for numero in range (x, y-1, -1):  # y-1= sposta lo stop al numero più basso di y che viene escluso, restituendo così y.
    print (numero)


# 13. Stampare a schermo la somma dei numeri da 1 a 10.
# CON FOR
somma = 0
for numero in range(1, 11):
    somma += numero  #somma incrementata con il numero scansionato --> somma= 1, somma= +2, somma= +3, ecc.
print(f"La somma è: {somma}")

#CON WHILE
somma= 0
numero= 1
while numero <= 10:
    somma += numero
    numero += 1
print (somma)


# 14. Stampare a schermo i numeri da 1 a 30 interropendo il ciclo quando si
#incontra il primo numero pari.
for x in range (1,31):
    print (x)
    if x % 2 == 0:
        break

# 15. Stampare a schermo i primi 10 numeri dispari.
for numero in range (1, 20, 2):
    print(numero)

#CON FOR
for numero in range (1, 20):
    if numero % 2 == 1:  #DISPARI vuol dire che diviso 2 da resto di 1.
        print (numero)

#CON WHILE
numero= 0
while numero <= 20:
    numero += 1
    if numero % 2 == 1:  #se il numero è dispari
     print(numero)


# 16. Stampare a schermo i primi 10 numeri pari.
for numero in range (2,21,2):
    print (numero)

#CON FOR
for numero in range (2,21):
    if numero %2 == 0:
        print (numero)

#CON WHILE
numero = 0
while numero <= 20:
    numero += 1
    if numero % 2 == 0:
        print (numero)
