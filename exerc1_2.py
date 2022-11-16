from unidecode import unidecode

# Exercicio 1
# Abrindo o arquivo txt1.txt
words = {}
with open('txt1.txt', 'r', encoding="utf8") as f:
    words = f.readlines()

# Remove as palavras repetidas
def remove_repetidos(lista):
    li = []
    for i in lista:
        if i not in li:
            li.append(i)
    li.sort()
    return li

# Remoção dos caracteres especiais
def remove_caracteres(char):
    vet2 = []
    for i in char:
        for j in i:
            vet2.append(unidecode(j).lower())
    return vet2

# Percorre as palavras, separa por espaço e adiciona lista em vet


def remove_char(wd):
    vet = []
    for word in wd:
        vet.append(word.replace(",", " ").replace(
            ".", " ").replace("\n", " ").split())
    return remove_caracteres(vet)


# Inicia
vet1 = remove_char(words)

# Gravação dos resultados em rs.txt
with open('rs.txt', 'w', encoding="utf8") as vetor:
    t = remove_repetidos(vet1)
    for i in t:
        print(i, file=vetor)

# ---------------------------------------------------------------------------------------------------------#
# Exercicio 2
aq_vocab = []
aq_doc = []
with open('rs.txt', 'r', encoding="utf8") as Entrada1, open('txt2.txt', 'r', encoding="utf8") as Entrada2:
    aq_vocab = Entrada1.readlines()
    aq_doc = Entrada2.readlines()

result = remove_char(aq_vocab)
result2 = remove_char(aq_doc)
r = []

# Gravação dos resultados em resultado_f'inal.txt
with open('resultado_final.txt', 'w', encoding="utf8") as final:
    for i in result:
        i.replace("\n", " ")
        
        if i in result2:
            r.append(1)
        else:
            r.append(0)
    print(r,file=final)
    final.close()
