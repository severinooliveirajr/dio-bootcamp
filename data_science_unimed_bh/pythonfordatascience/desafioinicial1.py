entrada = "200 3 8".split() #input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

# TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais no espaço #em branco abaixo:
icm = distancia / (diametro1 + diametro2)

print("Entrada: " + entrada[0] + ' ' + entrada[1] + ' ' + entrada[2])
print("ICM: " + "%.2f" % icm)