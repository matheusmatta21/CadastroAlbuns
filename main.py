from tkinter import *

#funcoes

def pegarDados():
    dados =[]
    dados.append(str(nomeAlbum.get()))
    dados.append(int(anoAlbum.get()))
    dados.append(str(nomeArtista.get()))
    dados.append(str(albumLancamento.get()))
    arquivo = open("dados.txt", "a", encoding='utf-8')
    for itens in dados:
        if dados.index(itens) == 3:
            arquivo.write(f"{itens}\n")
        else:
            arquivo.write(f"{itens}|")
    print(dados)
    arquivo.close()
    return dados



def vizualisarAlbuns():
    windowTwo = Tk()
    windowTwo.geometry("1000x550")
    labelPrincipal = Label(windowTwo, text='Lista de albuns:')
    labelPrincipal.pack()
    arquivo = open("dados.txt", 'r', encoding="utf-8")
    for linha in arquivo.readlines():
        album = linha.split('|')
        labelAlbum = Label(windowTwo, text=f"Album: {album[0]}\nAno: {album[1]}\nArtista: {album[2]}\nAlbum de Lançamento: {album[3]}")
        labelAlbum.pack()




#Gui

window = Tk()
window.title("Cadastro de Albuns")
window.geometry("500x250")
intro = Label(window, text="Insira as informações do album:")
intro.pack()

labelNomeAlbum = Label(window, text="Nome do album:")
labelNomeAlbum.place(x=130, y=30)


nomeAlbum = Entry(window, bd=2)
nomeAlbum.place(x=230, y=30)

labelAnoAlbum = Label(window, text="Ano do album:")
labelAnoAlbum.place(x=140, y=70)


anoAlbum = Entry(window, bd=2)
anoAlbum.place(x=230, y=70)

nomeArtista = Entry(window, bd=2)
nomeArtista.place(x=230, y=110)

labelNomeArtista = Label(window, text="Nome do artista/banda:")
labelNomeArtista.place(x=95, y=110)

albumLancamento = Entry(window, bd=2)
albumLancamento.place(x=230, y=150)


labelAlbumLancamemto = Label(window, text="Album de lançamento? (Sim/Não)")
labelAlbumLancamemto.place(x=40, y=150)

botaoConcluir = Button(window, text="Concluido", command=pegarDados)
botaoConcluir.place(x=220, y=190)

botaoVisualizarAlbuns = Button(window, text="Visualizar Albuns", command=vizualisarAlbuns)
botaoVisualizarAlbuns.place(x=220, y=220)

window.mainloop()

#transcrever dados para o arquivo .txt
