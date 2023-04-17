texto = input("Digite uma string: ")
texto_invertido = ""
for i in range(len(texto)-1, -1, -1):
    texto_invertido += texto[i]
print("String invertida:", texto_invertido)