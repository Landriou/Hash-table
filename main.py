from diccionary import *
from diccionaryDA import *
from linkedlist import *


D = Array(9,Diccionary())

dic_insert(D,28,28,H(28))
dic_insert(D,19,19,H(19))
dic_insert(D,6,6,H(6))
dic_insert(D,5,5,H(5))
dic_insert(D,3,3,H(3))
imprimirlista(D[H(28)])
imprimirlista(D[H(5)])
imprimirlista(D[H(6)])
print(dic_search(D,19,H(19)))
dic_delete(D,28,H(28))
print(dic_search(D,28,H(28)))

print("")
print("Ejercicio 4")
#Ejercicio 4
def IsPermutation(s,p):
    s = String(s) #Tomo la longitud mas larga
    p = String(p)
    if len(s) > len(p):
        size = len(s)
    else:
        size = len(p)
    if size % 2 == 0: #Evito que la longitud del hasttable sea par
        D = Array(size+1,Diccionary())
    else:
        D = Array(size,Diccionary())

    for n in range(len(s)): #Inserto ambos string letra por letra
        dic_insert(D,ord(s[n]),s[n],hashpermu(ord(s[n]),size))
    for i in range(len(p)):
        dic_insert(D,ord(p[i]),p[i],hashpermu(ord(p[i]),size))
    for j in range(size):  #Recorro el hastable y veo que todas las listas tengan longitud par
        if D[j] != None:
            if length(D[j]) % 2 != 0:
                return False
    return True #Si todas son pares, significa q es una permutacion

def hashpermu(k,size):
    return k % size

print(IsPermutation("hola","ah1l"))

#Ejercicio 5

def hasAllElementsUnique(lista):
    size = lista[0]
    for n in range(1,len(lista)):
        if size < lista[n]:
            size = lista[n]
    if size % 2 == 0: #Evito que la longitud del hasttable sea par
        D = Array(size+1,Diccionary())
    else:
        D = Array(size,Diccionary())
    for i in range(len(lista)):
        if D[hashpermu(lista[i],size)] == None:
            dic_insert(D,lista[i],lista[i], hashpermu(lista[i],size))
        else:
            return False #Si ya existe un elemento, es porque no es unico.
    return True
print("")
print("Ejercicio 5")
lista = Array(5,0)
lista[0] = 5
lista[1] = 4
lista[2] = 2
lista[3] = 2
lista[4] = 1
print(hasAllElementsUnique(lista))

#Ejercicio 6

def postalhash(k):
    String(k)
    hashstring = substr(k,1,4)
    hashint = int(hashstring)
    return hashint % 10000 #Con este numero cada una de las postales quedara en la lista que le corresponda a cada numero
    #Asi con la altura de las calles podemos averiguar cada postal

#Ejercicio 7
def stringCompresor(s):
    s = String(s)
    outstring = String("")
    contador = 1
    for n in range(len(s)):
        if n == len(s)-1:
            outstring = concat(outstring,s[n] + str(contador))
        else:
            if s[n+1] == s[n]:
                contador = contador + 1
            else:
                outstring = concat(outstring,s[n] + str(contador))
                contador = 1
    if len(outstring) > len(s):
        return s
    else:
        return outstring
print("")
print("Ejercicio 7")
ss = stringCompresor("aabcccccaaa")
print(ss)
s2 = stringCompresor("abc")
print(s2)
print("")
#Ejercicio 8
def hasOcurrency(S,P):
    S = String(S)
    P = String(P)
    cantletras = 0
    if len(P) > len(S):
        return False
    for n in range(len(S)):
        if S[n] == P[cantletras]:  #Si es la letra con la que empieza la palabra P
            cantletras = cantletras + 1
            if cantletras == len(P): #Si encontre todas las letras
                return True
        else:    #Si no lo vuelvo a cero
            cantletras = 0
        if S[n] == P[cantletras]: #Si se da el caso que la letra en que me pare es la primera letra de la palabra
            cantletras = cantletras + 1
    return False #Si llego a este punto retorna false
print("")
print("Ejercicio 8")
print(hasOcurrency("abracadabra","cada"))
print(hasOcurrency("abraccadabra","cada"))
print(hasOcurrency("abracadabra","cadi"))
print("")
print("Ejercicio 9")
#Ejercicio 9
def isIncluded(S,T):
    minimo = S[0]
    maximo = S[0]
    for n in range(1,len(S)):
        if minimo > S[n]:
            minimo = S[n]
        if maximo < S[n]:
            maximo = S[n]
    for i in range(len(T)): #Busco el minimo y el maximo entre los 2 conjuntos
        if minimo > T[i]:
            minimo = T[i]
        if maximo < T[i]:
            maximo = T[i]
    size = abs(maximo)+abs(minimo) + 1
    if size % 2 == 0: #Evito que la longitud del hasttable sea par
        D = Array(size+1,Diccionary())
    else:
        D = Array(size,Diccionary())
        
    for j in range(len(T)):
        dic_insert(D,T[j],T[j],hashIsIncluded(T[j],maximo,minimo))
    for k in range(len(S)):
        if D[hashIsIncluded(S[k],maximo,minimo)] == None: #Si encuenctro alguna posicion que no haya insertado
            return False #Quiere decir que son distintos, porque deberian caer todas en los mismos slots
    return True

def hashIsIncluded(k,maximo,minimo):
    size = abs(maximo) + abs(minimo) +1
    if k <= 0:
        return abs(k) % size
    else:
        return (k + abs(minimo)) % size

S = Array(5,0)
S[0] = -5
S[1] = 4
S[2] = 2
S[3] = 3
S[4] = 1
S3 = Array(3,0)
S3[0] = 5
S3[1] = 10
S3[2] = 20
T = Array(7,0)
T[0] = -5
T[1] = 4
T[2] = 3
T[3] = 2
T[4] = 1
T[5] = 6
T[6] = 7
print(isIncluded(S,T))
print(isIncluded(S3,T))

#Ejercicio 11
Diccio = Array(9,DiccionaryDA())
L = LinkedList()
DAsetup(Diccio,L)
insertDA(Diccio,L,1,H(0))
insertDA(Diccio,L,2,H(0))
insertDA(Diccio,L,3,H(0))

insertDA(Diccio,L,4,H(1))

