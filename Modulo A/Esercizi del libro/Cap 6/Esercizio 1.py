# CAP 3 ---------------------------------------------------------------------------------------------------------------------
# 10
def stampa_interi (int1=1, int2=2, int3=3,int4=4, int5=5):
     print(int1, int2, int3, int4, int5, sep=", ")  #ritorna numeri separati da virgola
print (stampa_interi ())

# 11
def stampa_str (str1="ciao", str2="mondo!") :
    print (str1, str2, sep=", ")
stampa_str()  # ciao, mondo!

# 12
def stampa_bool (var1=True, var2=False) :
    print (var1, var2, sep=", ")
stampa_bool()

# 13
def stampa_id (f1=1.2,f2=2.4,f3=3.8,f4=4.6,f5=5.2):
  print (id(f1), id(f2), id(f3), id(f4), id(f5))
stampa_id()

# 17
def stampa_tipo (f1=1.2,f2=2.4,f3=3.8,f4=4.6,f5=5.2):
    print (type(f1), type(f2), type(f3), type (f4), type(f5))
stampa_tipo()

# 21
def verifica_tipo (f1=1.2,f2=2.4,f3=3.8,f4=4.6,f5=5.2):
    print (isinstance(f1,float), isinstance(f2,float), isinstance(f3,float), isinstance(f4,float), isinstance(f5,float))
verifica_tipo()

# 26
def operazioni_e_id (int1=10, int2=20, int3=30,int4=40, int5=50):
    print (somma:= int1 + int2 + int3 + int4 + int5 + 100)
    print (sottrazione:= (int1+5)-(int2+5)-(int3+5)-(int4+5)-(int5+5))
    print (moltiplicazione:= int1 * int2 * int3 * int4 * int5)
    print (potenza:= int1**2 + int2**2 + int3**2 + int4**2 + int5**2)
    print (divisione:= int1 + int2 + int3 + int4 + int5 + 100 / 2)
    print (modulo:= int1%2, int2%2, int3%2, int4%2, int5%2)
    print (id(somma), id(sottrazione), id(moltiplicazione), id(potenza), id(divisione))

operazioni_e_id()

# 27
def concatena (str1="ciao", str2="mondo!"):
    concatenate = str1 + str2
    print (concatenate)
concatena()

# 28
def concatena (str1="ciao", str2="mondo!"):
    print (concatenate:= (str1 + str2) * 10)
    print ("lunghezza stringa: ", len (concatenate),"; singoli caratteri: ", concatenate[5], concatenate[4],concatenate[3])
concatena()

# 29
true=True
false=False
print (false1:=true and false, true1:=true and true, true2:=true or false, false2:=false or false, false3:=not true, true3:=not false)

# CAP 4 ----------------------------------------------------------------------------------------------------------------------------------------------------
# 1
def stampa_int ():
    for int in range (15, 122):
        print (int)
stampa_int()

# 2 e 3
def stampa_let () :
    alfabeto= "abcdefghijklmnopqrstuvz"
    a_m= alfabeto [:13]
    n_z= alfabeto [13: len(alfabeto)]
    print (a_m, n_z)
stampa_let()

# 4 e 5
def stampa_pari():
    for i in range (2,21,2):
        print (i)

def stampa_dispari():
    for i in range (1,20,2):
        print (i)
stampa_pari()
stampa_dispari()

# 6
def num_decrescenti ():
    for i in range (50, 39, -1):
        print (i)
num_decrescenti()

# 7 e 8
def quadrati_cubi():
    for i in range (1,11):
        quadrati= i **2
    for n in range (1,6):
        cubi= n ** 3
    print (quadrati, cubi)
quadrati_cubi()

# 9
def divisibili_100 ():
    for i in range (10,101,10):
        print (i)
divisibili_100()

# 10
def no_multipli_3():
    for i in range (1,21):
        if not i % 3 == 0:  #se non è multiplo di 3
            print (i)
no_multipli_3()

# 11
def stampa_numeri(num1,num2,num3) -> None: #perchè l'unico return è usato per il None
    if num1 < num2 and num3 < num2:
        for i in range (num1,num2+1):
            if i == num3:
                print (f"stampa interrotta perchè ho trovato il numero {num3}")
                return
            print (i)
    print("hai sbagliato qualcosa")

x= int(input("inserisci un numero: "))
y= int(input ("inserisci un numero: "))
z= int(input ("inserisci un numero: "))
stampa_numeri(x,y,z)

# 12
def stampa_numeri (num1, num2):
    for i in range (num1, num2-1, -1):
        print (i)

x= int(input("inserisci un numero: "))
y= int(input ("inserisci un numero: "))
stampa_numeri(x,y)

# 13
def somma ():
    somma=0
    for i in range (1,11):
        somma += i
        print (somma)
somma()

# 14
def stampa1_30 ():
    for i in range (1,31):
        if i%2==0: # se è pari
            return #interrompi il ciclo
        print (i)
stampa1_30()

# 15 e 16
def stampa_dispari():
    for i in range (1,11,2):
        print (i)

def stampa_pari():
    for i in range (0,11,2):
        print (i)

stampa_dispari()
stampa_pari()

# 17 Data una stringa inserita dall'utente, stampare tutti i CARATTERI della stringa
def stampa_caratteri(messaggio):
    tutti_caratteri= messaggio [::]  #così stampa INTERA stringa (non i caratteri uno a uno)
    print (tutti_caratteri)

str= input("Inserisci un messaggio: ")
stampa_caratteri(str)

#versione corretta:
def stampa_caratteri():
    messaggio= input("Inserisci un messaggio: ")
    for i in range (0, len(messaggio)):
        print (messaggio [i])
stampa_caratteri()

# 18 e 19
def stampa_caratteri():
    messaggio= input("Inserisci un messaggio: ")
    for i in range (0, len(messaggio), 2):
        print (messaggio[i])
stampa_caratteri()

def stampa_caratteri():
    messaggio= input("Inserisci un messaggio: ")
    for i in range (1, len(messaggio), 2):
        print (messaggio[i])
stampa_caratteri()

# 20
def stampa_coppia_caratteri ():
    messaggio= input("Inserisci un messaggio: ")
    for i in range (0, len(messaggio), 4):
        if i+1 < len(messaggio):
            print (messaggio[i]+messaggio[i+1]) #str e str si concatenano
    else:
        print (messaggio [i])
stampa_coppia_caratteri()

# 21
def stampa_caratteri ():
    messaggio= input("Inserisci un messaggio: ")
    for i in range (len(messaggio)-1, -1, -1):
        print (messaggio[i])
stampa_caratteri()

# CAP 5 -------------------------------------------------------------------------------------------------------------------------------------------------------------
#1
def estrai_4 (str="Imparo a programmare"):
    print (str [:4]) #solo stop
estrai_4()

# 2
def sottostringa (str= "Python è utile"):
    print (str[9:len(str)])
sottostringa()

# 3
def inverti(str= "ciao"):
    print (str[::-1])
inverti()

# 4 e 5
def caratteri_pari (str="Python è utile"):
    print (str[1::2])
caratteri_pari()

def caratteri_dispari (str="Python è utile"):
    print (str[::2])
caratteri_dispari()

# 6
def verifica (str= "info@gmail.com"):
    s= "@gmail.com"
    if s in str:
        print ("Indirizzo gmail")
    else:
        print ("indirizzo non riconosciuto")

# versione migliore:
def verifica (str= "info@gmail.com"):
    if str.endswith("@gmail.com"):
        print ("Indirizzo gmail")
    else:
        print ("indirizzo non riconosciuto")

# 7
def verifica (str= "Benvenuto su Python"):
    print (str.startswith("Benvenuto"))
verifica()

# 8
def contare(str= "abcabcabcabc"):
    numero_volte= str.count("abc")
    if numero_volte > 0:
        print (numero_volte)
contare()

# 9
def trovare (str= "Il sole splende alto nel cielo"):
    if str.find("cielo") >= len(str) - 10: #se la posizione di cielo è maggiore di quella del decimo carattere dalla fine.
        print ("Alla fine")
    else:
        print ("All'inizio")
trovare()

# 10 e 11
def maiuscolo (stringa="Python è interessante"):
    print (str.upper(stringa))
maiuscolo()

def minuscolo (stringa="PYTHON E INTERESSANTE"):
    print (str.lower(stringa))
minuscolo()

# 12 + rimuovere anche gli spazi intermedi.
def elimina_spazi (stringa= "   Pyt ho  n p   er t ut  ti   "):
    print (stringa. strip(). replace (" ", ""))
elimina_spazi()

# 13
def estrai (stringa= "Nome,Cognome,Età"):
    print (stringa.split(","))
estrai()

# 14 + modifica mia
def verifica_solo_lettere ():
    str= input("Inserisci un messaggio: ")
    if str.isalpha():
        print ("lettere")
    elif str.isdecimal():
        print("numeri")
    elif str.isalnum():
        print ("lettere e numeri")
    else:
        print ("contiene un carattere non identificato")  # es. ciao!
verifica_solo_lettere()

# 15
def fstring (s1,s2,s3,s4,s5):
    print (f"nome:{s1}, cognome:{s2}, età:{s3}, numero matricola:{s4}, numero di cellulare:{s5}")

dati = ("flavia", "burgio", 24, 8377278, 234365322)
fstring(*dati) #spacchetterà la tupla assegnando ciascun valore a ogni singolo parametro indicato




