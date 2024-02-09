import db


def pegarDados(nome, album, artista, lancamento):
    dados = []
    dados.append(str(nome))
    dados.append(int(album))
    dados.append(str(artista))
    dados.append(str(lancamento))
    db.registrarAlbum(dados)
    return dados 


def pegarAlbum(album):
    return db.lerAlbum(album)


def buscaPorAno(arquivo):
    return db.lerAlbum(arquivo)


def listarAnos(lista, album):
    db.lerAlbum(album)
    for i in range(0, len(album)):
        if album[i][1] in lista:
            pass
        else:
            lista.append(album[i][1])
    return lista
