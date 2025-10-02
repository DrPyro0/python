a=int(input("kérem az első számot: "))
b=int(input("\nKérem a második számot: "))
ment=a
"""
print(type(a))
"""


print("\nA értéke: ", a)
print("\nB értéke: ", b)
print("\nAz eredmény maradékos osztás esetén: ", a%b, "- Modulus")
print("\nAz eredmény egészrészes osztás esetén: ", a//b, "-Floor Division")
print("\nAz eredmény hatványozás esetén esetén: ", a**b, "- Exponantiation")

print("Összevont operátorok: ")

print("x=x+y helyett - x+=y")
a+=b
print(a)
a=ment

print("x=x-y helyett - x-=y")
a-=b
print(a)
a=ment

print("x=x*y helyett - x*=y")
a*=b
print(a)
a=ment

print("x=x/y helyett - x/=y")
a/=b
print(a)
a=ment

print("x=x//y helyett - x//=y")
a//=b
print(a)
a=ment

print("x=x%y helyett - x%=y")
a%=b
print(a)
a=ment

print("x=x**y helyett - x**=y")
a**=b
print(a)
a=ment