a=0
b=0
mjl=['+','-','*','/','**,','k'] #Ez a műveleti jel

mj=input("Kérem a műveleti jelet: ")
while mj != "k":
    if mj in mjl:
        a=int(input("Kérem az első számot: "))
        b=int(input("Kérem az második számot: "))
        if mj == '+':
            print("Az eredmény: ", a+b)
    elif mj == '-':
        print("Az eredmény: ", a-b)
    elif mj == '*':
        print("Az eredmény: ", a*b)
    elif mj == '/':
        print("Az eredmény: ", a/b)
    elif mj == '**':
        print("Az eredmény: ", a**b)
    else:
        print("Az ön által megadott művelet nem létezik")
        mj=input("Kérem a műveleti jelet: ")