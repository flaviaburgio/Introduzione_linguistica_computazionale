var1= 10
var2= 2
variabile_con_nome_lungo1=0
variabile__= 10
non_lo_so123= 82

#Con più variabili dobbiamo assegnare ogni id() a una variabile separata prima di stamparle
id_variabile1 = id (var1)
posizione = id (var2)
posizione_o_id_variabile3 = id (variabile_con_nome_lungo1)
id_variabile4 = id (variabile__)
id_variabile5 = id (non_lo_so123)
print (id_variabile1, posizione, posizione_o_id_variabile3, id_variabile4, id_variabile5)

#QUANDO ABBIAMO UNA SOLA VARIABILE POSSIAMO RIASSUMERE COSI:
altra_variabile= "ciaoooo"
print (id(altra_variabile))

#QUANDO AGGIORNIAMO UN TIPO IMMUTABILE, IL NUOVO VALORE VIENE SALVATO IN UN NUOVO SPAZIO DI MEMORIA!
valore= 10
print (id(valore))
valore = valore + 1   #11
print (valore)
print (id(valore))

