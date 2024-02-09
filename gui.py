from tkinter import *
from tkinter.ttk import Combobox
import domain


def visualizarAlbuns():
    def buscarPorNome():
        windowThree = Tk()
        windowThree.geometry = "1000x500"
        albumNome = []
        albumBuscado = inputAlbumBuscado.get()
        domain.pegarAlbum(albumNome)
        for i in range(0, len(albumNome)):
            if albumBuscado in albumNome[i][0]:
                labelAlbumBuscado = Label(
                    windowThree,
                    text=f"Album: {albumNome[i][0]}\nAno: {albumNome[i][1]}\nArtista: {albumNome[i][2]}\nAlbum de Lançamento: {albumNome[i][3]}",
                )
                labelAlbumBuscado.pack()
            else:
                continue
        windowThree.mainloop()

    def buscarPorAno():
        windowFour = Tk()
        windowFour.geometry("1000x550")
        labelPrincipal2 = Label(windowFour, text="Lista de albuns:")
        labelPrincipal2.pack()
        opcaoEscolhida = valorEscolha.get()
        anoEscolhido = comboboxAnos.get()
        albuns = []
        domain.buscaPorAno(albuns)
        for i in range(0, len(albuns)):
            if opcaoEscolhida == 0:
                if anoEscolhido >= albuns[i][1]:
                    labelAlbumAno = Label(
                        windowFour,
                        text=f"Album: {albuns[i][0]}\nAno: {albuns[i][1]}\nArtista: {albuns[i][2]}\nAlbum de Lançamento: {albuns[i][3]}",
                    )
                    labelAlbumAno.pack()
            elif opcaoEscolhida == 1:
                if anoEscolhido == albuns[i][1]:
                    labelAlbumAno = Label(
                        windowFour,
                        text=f"Album: {albuns[i][0]}\nAno: {albuns[i][1]}\nArtista: {albuns[i][2]}\nAlbum de Lançamento: {albuns[i][3]}",
                    )
                    labelAlbumAno.pack()
            elif opcaoEscolhida == 2:
                if anoEscolhido <= albuns[i][1]:
                    labelAlbumAno = Label(
                        windowFour,
                        text=f"Album: {albuns[i][0]}\nAno: {albuns[i][1]}\nArtista: {albuns[i][2]}\nAlbum de Lançamento: {albuns[i][3]}",
                    )
                    labelAlbumAno.pack()
        windowFour.mainloop()

    windowTwo = Tk()
    windowTwo.geometry("1000x550")
    labelPrincipal = Label(windowTwo, text="Lista de albuns:")
    labelPrincipal.pack()
    album = []
    domain.pegarAlbum(album)
    for i in range(0, len(album)):
        labelAlbum = Label(
            windowTwo,
            text=f"Album: {album[i][0]}\nAno: {album[i][1]}\nArtista: {album[i][2]}\nAlbum de Lançamento: {album[i][3]}",
        )
        labelAlbum.pack()
    labelInputAlbum = Label(windowTwo, text="Buscar album por nome:")
    labelInputAlbum.place(x=160, y=20)

    inputAlbumBuscado = Entry(windowTwo, bd=2)
    inputAlbumBuscado.place(x=300, y=20)

    botaoBuscarNome = Button(windowTwo, text="Buscar", command=buscarPorNome)
    botaoBuscarNome.place(x=230, y=45)

    labelInputAno = Label(windowTwo, text="Buscar por ano:")
    labelInputAno.place(x=160, y=100)



    # o valorEscolha não está sendo atribuido ao opcaoEscolhida = valorEscolha.get(). tentei procurar tudo que é possivel pra corrigir isso, mas não obtive solução alguma.
    valorEscolha = IntVar()
    r1 = Radiobutton(windowTwo, text="Anterior a", value=0, variable=valorEscolha)
    r2 = Radiobutton(windowTwo, text="Igual a", value=1, variable=valorEscolha)
    r3 = Radiobutton(windowTwo, text="Posterior a", value=2, variable=valorEscolha)
    r1.place(x=160, y=130)
    r2.place(x=160, y=150)
    r3.place(x=160, y=170)

    listaAnos = []
    domain.listarAnos(listaAnos, album)
    comboboxAnos = Combobox(windowTwo, values=listaAnos)
    comboboxAnos.place(x=250, y=100)

    botaoBuscarAno = Button(windowTwo, text="Buscar Ano", command=buscarPorAno)
    botaoBuscarAno.place(x=250, y=150)

    windowTwo.mainloop()



def main():
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

    botaoConcluir = Button(
        window,
        text="Concluido",
        command=lambda: domain.pegarDados(
            nomeAlbum.get(), anoAlbum.get(), nomeArtista.get(), albumLancamento.get()
        ),
    )
    botaoConcluir.place(x=220, y=190)

    botaoVisualizarAlbuns = Button(
        window, text="Visualizar Albuns", command=visualizarAlbuns
    )
    botaoVisualizarAlbuns.place(x=210, y=220)

    window.mainloop()


if __name__ == "__main__":
    main()
