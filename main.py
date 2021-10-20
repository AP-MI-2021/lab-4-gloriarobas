def print_meniu():
    print("1. Citire lista")
    print("2. Toate numerele negative nenule din lista")
    print("3. Cel mai mic numar cu ultima cifra citita de la tastatura")
    print("4. Toate numerele din lista care sunt superprime")
    print("5. Modificare lista")
    print("6. Iesire")

def citire_lista():
    list=[]
    n = int(input("Numarul de elemente:"))
    for i in range(n):
        list.append(int(input()))
    return list

def neg_nenul(x):
    if x<0:
        return True
    return False

def numere_negative(list):
    lista_negative=[]
    for x in list:
        if neg_nenul(x)==True:
            lista_negative.append(x)
    return lista_negative

def test_cerinta2():
    assert numere_negative([1, -3, 9, -6])==[-3,-6]
    assert numere_negative([-8, -9, 12])==[-8,-9]

def ultima_cifra(n,list):
    rez_partial = 999999
    for x in list:
        if x%10==n and x<rez_partial:
            rez_partial=x
    return rez_partial

def test_cerinta3():
    assert ultima_cifra(9,[29, 49, 13]) == 29
    assert ultima_cifra(2,[52, -9, 12]) == 12

def prim(p):
    if p<2:
        return False
    else:
        for i in range(2,p//2+1):
            if p%i==0:
                return False
    return True

def test_prim():
    assert prim(7)==True
    assert prim(15)==False
    assert prim(29)==True

def superprim(a):
    ok=1
    while a!=0:
        if a<0 or prim(a)==False:
            ok=0
        a=a//10
    if ok==1:
        return True
    return False

def test_superprim():
    assert superprim(173)==False
    assert superprim(239)==True

def toate_superprime(list):
    rez = []
    for x in list:
        if superprim(x)==True:
            rez.append(x)
    return rez

def test_cerinta4():
    assert toate_superprime([239, 23, 17])==[239,23]
    assert toate_superprime([29,139,48])==[29]

def cmmdc(a,b):
    while (a != b):
        if (a > b):
            a = a - b
        else:
            b = b - a
    return a

def test_cmmdc():
    assert cmmdc(12,24)==12
    assert cmmdc(13,5)==1

def oglindit(n):
    nr=0
    numar=abs(n)
    while numar!=0:
        nr=nr*10+numar%10
        numar=numar//10
    return -nr

def test_oglindit():
    assert oglindit(-37)==-73
    assert oglindit(-76)==-67
    assert oglindit(-13)==-31

def inlocuire(list):
    rezultat=[]
    pozitive=[]
    for x in list:
        if x>0:
            pozitive.append(x)
    a=pozitive[0]
    b=pozitive[1]
    c=cmmdc(a,b)
    i=2
    while i<len(pozitive):
        if pozitive[i]%c!=0:
            c=cmmdc(c,pozitive[i])
        i=i+1
    for x in list:
        if x>0:
            rezultat.append(c)
        else:
            rezultat.append(oglindit(x))
    return rezultat

def test_cerinta5():
    assert inlocuire([-76, 12, 24, -13, 144]) == [-67, 12, 12, -31, 12]

def main():
    list=[]
    while True:
        print_meniu()
        option = int(input("Alegeti optiunea:"))
        if option == 1:
            list = citire_lista()
        elif option == 2:
            rezultat=numere_negative(list)
            print(rezultat)
        elif option==3:
            cifra = int(input("Dati cifra"))
            print(ultima_cifra(cifra,list))
        elif option==4:
            print(toate_superprime(list))
        elif option==5:
            print(inlocuire(list))
        elif option == 6:
            break
        else:
            print("optiune invalida ! Reincercati !")
    test_prim()
    test_cerinta3()
    test_cerinta2()
    test_cmmdc()
    test_superprim()
    test_cerinta4()
    test_oglindit()
    test_cerinta5()

if __name__ == '__main__':
    main()
