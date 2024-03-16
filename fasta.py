cabecalho = input("Informe o cabeçalho da sequência: ")
sequencia = input("Informe a sequencia de aminoacidos: ")

file = open("arq2.txt", "w")

file.write(">" + cabecalho + "\n")
file.write(sequencia)

file.close()