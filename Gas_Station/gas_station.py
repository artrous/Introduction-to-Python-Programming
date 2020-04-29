kaysimo=["βενζίνη super","βενζίνη αμόλυβδη","πετρέλαιο"]
timi_pol=[0,0,0] # λιστα για τα αθροίσματα πώλησης τιμής καυσίμου
plithos=[0,0,0] # λίστα για πλήθος πώλησης κάθε κατηγορίας καυσίμου
epan=True # αρχική τιμή για την είσοδο στην επανάληψη
pl=0
while epan:
    afm=input("ΑΦΜ εμπόρου ή 000000000 για τέλος επεξεργασίας: ")
    if afm!='000000000':
        eponymo=input("Ονοματεπώνυμο εμπόρου: ")
        lathos=True # αρχική τιμή για την είσοδο στην επανάληψη
        while lathos:
            eidos=int(input("ειδος καυσίμου: 1=βενζίνη super, 2=βενζίνη αμόλυβδη, 3=πετρέλαιο: "))
            if eidos==1 or eidos==2 or eidos==3:
                lathos=False
        lathos=True
        while lathos: # αρχική τιμή για την είσοδο στην επανάληψη
            timi_a=float(input("τιμή αγοράς: "))
            if timi_a>0:
                lathos=False
        lathos=True
        while lathos: # αρχική τιμή για την είσοδο στην επανάληψη
            timi_p=float(input("τιμή πώλησης: "))
            if timi_p>0:
                lathos=False
        p_kerdous=100*(timi_p-timi_a)/timi_a # υπολογισμός ποσοστού κέρδους
        if p_kerdous>12:
            print(afm,eponymo,kaysimo[eidos-1],timi_a,timi_p)
            pl+=1
        timi_pol[eidos-1]+=timi_p
        plithos[eidos-1]+=1
    else:
        epan=False
print("Aποτελέσματα")
print("πλήθος με ποσοστό κέρδους >12%: ", pl)
for i in range(3):
    if plithos[i]>0:
        mt=timi_pol[i]/plithos[i]
        print(kaysimo[i],mt)
