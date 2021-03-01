1) 
nome = input("Inserisci il tuo nome: ")
print (nome)

2)
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
print (nome , cognome)

3)
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
print (len(nome), len(cognome))

4)
x = input("Inserisci il primo numero: ")
y = input("Inserisci il secondo numero: ")

if x > y: print (x , y)
else: print (y, x)

5)
colore = input("Inserisci il tuo colore preferito: ")
if colore == "nero" or colore == "NERO" or colore == "Nero": print("Bello")
else: print("Non mi piace")

6)
nome = input("Inserisci il tuo nome: ")
c=0
while(c<3): 
  print(nome)
  c+=1

7)
nome = input("Inserisci il tuo nome: ")

for x in nome:
  print(x)

8)
frutta = ("Arancia", "Cocco", "Ananas", "Banana")
print(frutta[2])

9)
frutta = ("Arancia", "Cocco", "Ananas", "Banana")
print(frutta)
scelta = input("Scegli uno di questi quattro: ")
if scelta == "Arancia": 
  print(frutta.index("Arancia"))

if scelta == "Cocco": 
  print(frutta.index("Cocco"))

if scelta == "Ananas": 
  print(frutta.index("Ananas"))

if scelta == "Banana": 
  print(frutta.index("Banana"))

10)
list = ["Luigi", "Frank" , "Paolo" , "Marco", "Giovanni"]

c = 0
while c < len(list):
  print(list[c])
  c += 1

11)
list = ["Luigi", "Frank" , "Paolo" , "Marco", "Giovanni", "Luca", "Antonio", "Mena", "Mario", "Federica"]
list.sort()
c = 0
while c < len(list):
  print(list[c])
  c += 1
