# 9
# con Tupla
def media_voti (lista:list)-> int| float:
    tot_voti=0
    tot_studenti=0
    for tupla in lista:
        tot_voti += tupla[1]
        tot_studenti += 1
    media= tot_voti/tot_studenti
    return media

lista= [("Flavia",110), ("Luca", 105), ("Marco", 94)]
print (media_voti(lista))

# con Dizionario
def media_voti (diz:dict) -> int|float:
    lista_voti= diz["Voto"]  #[110, 105, 94]
    somma_voti =0
    numero_studenti= len(lista_voti) #3 voti, 3 studenti.

    for voto in lista_voti:
        somma_voti += voto

    media= somma_voti/numero_studenti
    return media

diz= {
    "Nome": ["flavia","luca","marco"],
    "Voto": [110,105,94]
}
print (media_voti(diz))

# 10
# tupla
def studenti_eccellenti (lista:list)->list:
    studenti_eccellenti= []
    for tupla in lista:
        if tupla[1]>100:
            studenti_eccellenti.append(tupla[0])
    return studenti_eccellenti

dati= [("Flavia",110), ("Luca", 105), ("Marco ", 94)]
print(studenti_eccellenti(dati))

# dizionario
def studenti_eccellenti(lista:list) -> list:
    eccellenti= []
    for diz in lista:   #prende ciascun dizionario
        if diz["Voto"]>100:
            eccellenti.append(diz["Nome"])

    return eccellenti

dati= [ {"Nome": "flavia", "Voto":110},
        {"Nome": "luca", "Voto":101},
        {"Nome": "marco", "Voto":94}
]
print(studenti_eccellenti(dati))

# 11
# tupla
def studenti_eccellenti_con_voto (lista:list):
    risultato= []
    for tupla in lista:
        if tupla[1] >=100:
            risultato.append( (tupla[0], tupla[1]) )
    return risultato


dati= [("Flavia",110), ("Luca", 105), ("Marco", 94)]
print (studenti_eccellenti_con_voto(dati))


# dizionario
def studenti_eccellenti_con_voto (lista:list):
    risultato= []
    for diz in lista:
        if diz ["Voto"] >= 100:
            risultato.append ( (diz["Nome"], diz["Voto"]) )
    return risultato

dati= [ {"Nome": "flavia", "Voto":110},
        {"Nome": "luca", "Voto":101},
        {"Nome": "marco", "Voto":94} ]
print(studenti_eccellenti_con_voto(dati))

# 12 - MEDIA VOTO PER OGNI CORSO
def media_per_corso (lista:list) -> str:
    #voti ogni corso
    voti_lettere= 0
    voti_comunicazione= 0
    voti_SDT= 0
    #numero studenti
    tot_stud_lettere=0
    tot_stud_comunicazione=0
    tot_stud_SDT=0

    for tupla in lista:

        if tupla[2]=="Lettere":
            voti_lettere+=tupla[1]
            tot_stud_lettere+=1

        elif tupla[2]=="Comunicazione":
            voti_comunicazione+=tupla[1]
            tot_stud_comunicazione+=1

        elif tupla[2]=="SDT":
            voti_SDT+=tupla[1]
            tot_stud_SDT+=1

    return f"Medie: Lettere: {voti_lettere/tot_stud_lettere}, Comunicazione {voti_comunicazione/tot_stud_comunicazione}, SDT: {voti_SDT/tot_stud_SDT}"

dati=[("Tizio", 96, "Lettere"), ("Caio", 102, "Comunicazione"),
      ("Sempronio", 90, "SDT"), ("Mario", 100, "SDT"),
      ("Erica", 105, "Comunicazione"), ("Paola", 110, "Lettere")]

print(media_per_corso(dati))

# 13
# con lista di tuple
def media_voti_per_docente_e_corso(studenti, docenti) -> str:
    #voti per materia
    voti_matematica=[]
    voti_fisica=[]
    voti_chimica=[]  #per la media faccio sum(lista)/ len(lista)
    #docenti per materie
    docente_matematica=""
    docente_fisica=""
    docente_chimica=""

    for tupla in studenti:
        if tupla[2]=="Matematica":
            voti_matematica.append(tupla[1])
        elif tupla[2]=="Fisica":
            voti_fisica.append(tupla[1])
        elif tupla[2]=="Chimica":
            voti_chimica.append(tupla[1])

    for tupla in docenti:
        if tupla[1]=="Matematica":
            docente_matematica+= tupla[0]
        elif tupla[1]=="Fisica":
            docente_fisica+= tupla[0]
        elif tupla[1]=="Chimica":
            docente_chimica+= tupla[0]

    return (f"Matematica {docente_matematica}: media voti: {sum(voti_matematica)/len(voti_matematica):.2f},\n"
            f"Fisica {docente_fisica}: media voti: {sum(voti_fisica)/len(voti_fisica):.2f},\n"
            f"Chimica {docente_chimica}: media voti {sum(voti_chimica)/len(voti_chimica):.2f}.")


studenti = [("Alice", 28, "Matematica"),("Bob", 30, "Fisica"),
        ("Carla", 26, "Matematica"),("Daniele", 27, "Fisica"),
        ("Elena", 29, "Chimica")]

docenti = [("Prof. Rossi", "Matematica"),("Prof. Bianchi", "Fisica"),
        ("Prof.ssa Verdi", "Chimica")]

print (media_voti_per_docente_e_corso(studenti, docenti))

# 14
def docente_voti_piu_alti (studenti:list, docenti:list):
    #tot voti per materia
    voti_mate=[]
    voti_fisica=[]
    voti_chimica=[]

    #docenti per materia
    docente_matematica=""
    docente_fisica=""
    docente_chimica=""

    for tupla in studenti:
        if tupla[2]=="Matematica":
            voti_mate.append(tupla[1])
        elif tupla[2]=="Fisica":
            voti_fisica.append(tupla[1])
        elif tupla[2]=="Chimica":
            voti_chimica.append(tupla[1])

    for tupla2 in docenti:
        if tupla2[1]=="Matematica":
            docente_matematica= tupla2[0]
        elif tupla2[1]=="Fisica":
            docente_fisica= tupla2[0]
        elif tupla2[1]=="Chimica":
            docente_chimica= tupla2[0]

    media_mate= sum(voti_mate)/len(voti_mate)
    media_fisica= sum(voti_fisica)/len(voti_fisica)
    media_chimica=sum(voti_chimica)/len(voti_chimica)

    #trovare la media più alta usando max()
    media_max= max(media_mate, media_fisica, media_chimica)

    if media_max == media_mate:
        return f"{docente_matematica} mette i voti più alti, in media: {media_mate:.2f}"
    elif media_max == media_fisica:
        return f"{docente_fisica} mette i voti più alti, in media: {media_fisica:.2f}"
    else:
        return f"{docente_chimica} mette i voti più alti, in media: {media_chimica:.2f}"


studenti = [("Alice", 28, "Matematica"),("Bob", 30, "Fisica"),
        ("Carla", 26, "Matematica"),("Daniele", 27, "Fisica"),
        ("Elena", 29, "Chimica"), ("Giulia",18, "Chimica")]

docenti = [("Prof. Rossi", "Matematica"),("Prof. Bianchi", "Fisica"),
        ("Prof.ssa Verdi", "Chimica")]

print(docente_voti_piu_alti(studenti, docenti))

# 15
def crea_dizionari (lista:list) -> list:
    risultato= []
    for stringa in lista:
        lista1= stringa.split(",")
        diz= {"Nome": lista1[0].strip(), "Cognome": lista1[1].strip(), "Data": lista1[2].strip()}
        risultato.append(diz)
    return risultato

dati= ["Mario   ,       Rossi    , 01/01/2000",
    "Luca, Bianchi,         15/03/1999  ",
    "Anna, Verdi, 20/05/2001"]
print(crea_dizionari(dati))

# 16
def crea_dizionari (lista1:list, lista2:list) -> list:
    risultato = []

    # Ciclo su tutti gli indici della prima lista
    for pos in range(len(lista1)):
        elementi_stringa = lista1[pos].split(" ")

        diz = {"NOME_COMPLETO": (elementi_stringa[0], elementi_stringa[1]),
            "DATA_NASCITA": lista2[pos]}

        risultato.append(diz)

    return risultato


#[{"NOME_COMPLETO": (), "DATA_NASCITA": }]
lista1=["Mario Rossi", "Fabrizio Bianchi", "Giulia Amanti"]
lista2=["01/01/2000", "17/06/1976", "15/9/2003"]

print(crea_dizionari(lista1, lista2))
