def registrarAlbum(lista):
    with open("dados.txt", "a", encoding="utf-8") as arquivo:
        for itens in lista:
            if lista.index(itens) == 3:
                arquivo.write(f"{itens}\n")
            else:
                arquivo.write(f"{itens}|")


def lerAlbum(lista):
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            lista.append(linha.split("|"))
        print(lista)
    return lista
