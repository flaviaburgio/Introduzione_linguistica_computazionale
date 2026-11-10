vero1= True
vero2= True
falso1= False
falso2= False

#AND
and1= vero1 and vero2 #TRUE
and2= vero1 and falso1  #FALSE

21 > 1 and 3 < 5 #TRUE AND TRUE
True
22 == 22 and 1 > 2 #TRUE AND FALSE
False
2 < 1 and "asd" == "asd" #FALSE AND TRUE
False
23 == 15 and 33 != 33  #FALSE AND FALSE
False

#OR
or1= vero1 or vero2 #TRUE
or2=vero1 or falso2  #TRUE
or3= falso1 or falso2  #FALSE

25 >= 25 or 23 <= 25  #TRUE OR TRUE
True
"io" == "io" or "io" == "robot"  #TRUE OR FALSE
True
1 != 1 or 1 == 1  # FALSE OR TRUE
True
4 == 5 or 5 == 6  # FALSE OR FALSE
False

#NOT
not1= not vero1 #FALSE
not2= not falso1 #TRUE
print (and1, and2, or1, or2, or3, not1, not2)

