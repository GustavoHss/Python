menu = 0

def abrirArquivo():
    nome = input("Digite o nome do aquivo desejado: ")

    arquivo = open(nome)

    return arquivo

def lerArquivo(arquivo):
    linhas = arquivo.readlines()

    for linha in linhas:
        print(linha.strip())

while menu != 3:
    print("1 - Abrir arquivo\n2 - Ler aquivo\n3 - Sair\n")
    menu = int(input("Informe uma das opções cima: "))

    if menu == 1:
        arquivo = abrirArquivo()
    
    elif menu == 2:
        lerArquivo(arquivo)