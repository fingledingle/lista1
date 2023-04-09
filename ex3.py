#pedir os dois numeros
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input ("Digite o segundo numero: "))

#calcular produto
produto = num1 * num2

#print se e par ou impar

if produto % 2 == 0:
    print ("O numero", produto, "e par")
else:
    print ("O numero", produto, "e impar")
