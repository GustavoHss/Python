arquivo = open("arq2.txt")

linhas = arquivo.readlines()
multi_fasta = {}

for linha in linhas:
    if linha[0] == ">":
        seq_atual = linha.strip()
        multi_fasta[seq_atual] = ""
    else:
        multi_fasta[seq_atual] = multi_fasta[seq_atual] + linha.strip()

print(multi_fasta[">123456"])