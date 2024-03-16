arquivo = input("Informe o nome do arquivo: ")

file = open(arquivo)

texto_completo = file.read()

print(texto_completo)

file.close()