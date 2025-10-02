import math

a=pow(math.pi,2)
print("Ez a pi négyzet formázás nélkül: ", a)
print("Ez a pi négyzet formázása: ", f"{a:.4f}")
print("Szorozzuk 10000-rel: ",10000*a)
a=round(a,3)
print("Szorozzuk 10000-rel: ",10000*a)