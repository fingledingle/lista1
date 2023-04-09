#pedir o nome, sexo e estado civil
nome = input("Digite o nome da pessoa: ")
sexo = input("Digite o sexo da pessoa (M/F): ")
estado_civil =  input("Digite o estado civil: ")

#If pra ver por quanto tempo a pessoa e casa

if sexo == "F" and estado_civil == "CASADA":
    anos_casada = input("Tempo de casada: ")
    print ("A", nome, "e casada ha", anos_casada, "anos")
else:
    print ("A pessoa", nome, "nao e casada") 




