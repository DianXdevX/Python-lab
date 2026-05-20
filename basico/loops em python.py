#loops em python 
#for loop 
for numero in range(1, 11):
    print(numero)
#while  loop 
contador = 1 #var name

while contador <= 5:
    print(contador)
    contador += 1
#continue  inginora uma instacia 
#break  para o loop 
#else  se  o atributo  nao conresponder  tal  coisa ocorre
#Tipos de loop em Python:
#- for
#- while

#Comandos de controle:
#- break
#- continue
#- else
#exemplo de funçao com loops 
def exp(x):
    for x in range(10):
        print(x)

    while x > 0:
        print("x irá se tornar zero")
        x = x - 1

        if x == 0:
            print("zero")
exp(10)