# definir as aliquotas do imposto de renda
aliquotas = {
    0: 0,
    1903.98: 0,
    2826.65: 0.075,
    3751.05: 0.15,
    4664.68: 0.225,
    float("inf"): 0.275
}

# ler os dados dos indivíduos
num_individuos = int(input("Digite o numero de individuos: "))
for i in range(num_individuos):
    nome = input(f"Digite o nome do {i+1}º individuo: ")
    renda = float(input(f"Digite a renda do {i+1}º individuo: "))

    # Calcular a alíquota de imposto de renda do individuo
    for limite, aliquota in aliquotas.items():
        if renda <= limite:
            deducao = renda * aliquota
            break

    # Imprimir a alíquota de IR do individuo
    print(f"A aliquota de deduçao do imposto de renda do(a) {nome} e de R$ {deducao:.2f}.")
