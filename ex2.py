#pedir os tamanho dos lados
a = float(input("Tamanho do lado a: "))
b = float(input("Tamanho do lado b: "))
c = float(input("Tamanho do lado c: "))

# classificacao do triangulo e print na tela
if a == b == c:
    print("O triangulo e equilatero")
elif a == b or b == c or a == c:
    print("O triangulo e isoceles")
else:
    print("O triangulo e escaleno")