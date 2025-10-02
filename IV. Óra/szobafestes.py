m=2.3
s=3.2
h=4.8
fdml=[1, 3, 5, 10]
print("A szoba falainak terület:", m*s*h,"m2",)
print("A festék kiadóssága:0,3 kg/m2")
fdm=int(input("Hány kilós a festék dobozod?"))
if fdm in fdml:
    if fdm >= 1 <10:
        print("Nem elég a festéked")
    else:
        print("A legnagyobb festékes dobozpd se elegendő")
else:
    print("Válassz egy olyan festékes dobozt ami neked van")
