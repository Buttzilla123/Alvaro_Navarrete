SW1native = 99
SW2native = 200
SW1Vlan = 10,20,30
SW2Vlan = 40,50,60
SW1imag = 10,100,30
SW2nonat = 99
SW2vlansdia = 40,50,60
if SW1native == SW2native:
    print ("las vlans son iguales y cumplen el requerimiento")
else:
    print ("Las vlans nativas de ambos switchs son diferentes")

if SW1Vlan == SW1imag:
    print ("las vlans son iguales y cumplen con el requerimiento")
else:
    print ("las vlans de SW1 no son las mismas del diagrama")
if SW2native == SW2nonat:
    print ("ambas vlans nativas son iguales")
else:
    print ("La vlan nativa de SW2 no es la misma del diagrama")
if SW2Vlan == SW2vlansdia:
    print("las vlans en SW2 son las mismas que las del diagrama")
else:
    print ("no son las mismas")