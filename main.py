from tkinter import *
from tkinter.ttk import Combobox
#variaveis de armazenamento de dados


#funcoes de pegar dados // validar, tratar erros, criar funcoes separadas pra formatacao 

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
    return dados #estudar melhor os returns das funcoes


def visualizarAlbuns(): #if len(listaAlbuns) == 0: erro
    def buscarPorNome():
        windowThree= Tk()
        windowThree.geometry =("1000x500")
        arquivo = open("dados.txt", "r", encoding="utf-8")
        for linhas in arquivo.readlines():
            album = linhas.split("|")
            if inputAlbumBuscado.get() in album[0]:
                labelAlbumBuscado = Label(windowThree, text=f"Album: {album[0]}\nAno: {album[1]}\nArtista: {album[2]}\nAlbum de Lançamento: {album[3]}")
                labelAlbumBuscado.pack()
            else:
                continue
        arquivo.close() 
        
        windowThree.mainloop()

    def buscarPorAno():
        windowFour = Tk()
        windowFour.geometry("1000x550")
        labelPrincipal2 = Label(windowFour, text='Lista de albuns:')
        labelPrincipal2.pack()
        opcaoEscolhida = valorEscolha.get()
        anoEscolhido = comboboxAnos.get()
        arquivoAnos = open("dados.txt", "r", encoding="utf-8")
        print(opcaoEscolhida)
        if opcaoEscolhida == 1:
            for linhas in arquivoAnos.readlines():
                albuns = linhas.split('|')
                print(albuns[1])
                if anoEscolhido >= albuns[1]:
                    labelAlbumAno = Label(windowFour,text=f"Album: {albuns[0]}\nAno: {albuns[1]}\nArtista: {albuns[2]}\nAlbum de Lançamento: {albuns[3]}")
                    labelAlbumAno.pack()
            arquivoAnos.close()
        elif opcaoEscolhida == 4:
            for linhas in arquivoAnos.readlines():
                albuns = linhas.split('|')
                if anoEscolhido == albuns[1]:
                    labelAlbumAno = Label(windowFour,text=f"Album: {albuns[0]}\nAno: {albuns[1]}\nArtista: {albuns[2]}\nAlbum de Lançamento: {albuns[3]}")
                    labelAlbumAno.pack()
            arquivoAnos.close()
        elif opcaoEscolhida == 0:
            for linhas in arquivoAnos.readlines():
                albuns = linhas.split('|')
                if anoEscolhido <= albuns[1]:
                    labelAlbumAno = Label(windowFour,text=f"Album: {albuns[0]}\nAno: {albuns[1]}\nArtista: {albuns[2]}\nAlbum de Lançamento: {albuns[3]}")
                    labelAlbumAno.pack()
            arquivoAnos.close()
            
        windowFour.mainloop()

    windowTwo = Tk()
    windowTwo.geometry("1000x550")
    labelPrincipal = Label(windowTwo, text='Lista de albuns:')
    labelPrincipal.pack()
    arquivo = open("dados.txt", 'r', encoding="utf-8")
    for linha in arquivo.readlines():
        album = linha.split('|')
        labelAlbum = Label(windowTwo,text=f"Album: {album[0]}\nAno: {album[1]}\nArtista: {album[2]}\nAlbum de Lançamento: {album[3]}")
        labelAlbum.pack()
    arquivo.close()
    labelInputAlbum = Label(windowTwo, text="Buscar album por nome:")
    labelInputAlbum.place(x= 160, y=20)

    inputAlbumBuscado = Entry(windowTwo, bd=2)
    inputAlbumBuscado.place(x=300,y=20)

    botaoBuscarNome = Button(windowTwo, text="Buscar", command=buscarPorNome)
    botaoBuscarNome.place(x=230,y=45)

    labelInputAno = Label(windowTwo, text="Buscar por ano:")
    labelInputAno.place(x=160, y=100)

    #organizar melhor a parte da combobox, criar uma def com variavel global da listaAnos

    listaAnos = []
    arquivo = open("dados.txt", "r", encoding='utf-8')
    for linha in arquivo.readlines():
        album = linha.split("|")
        listaAnos.append(album[1])
    listaAnos.sort()
    arquivo.close()
    comboboxAnos = Combobox(windowTwo, values=listaAnos)
    comboboxAnos.place(x=250, y= 100)

    #tudo certo, porem nao atribui o valor da radio pra variavel
    valorEscolha = IntVar()
    r1 = Radiobutton(windowTwo, text="Anterior a", value = 0, variable = valorEscolha)
    r2 = Radiobutton(windowTwo, text="Igual a", value = 1, variable = valorEscolha)
    r3 = Radiobutton(windowTwo, text="Posterior a", value = 2, variable = valorEscolha)

    r1.place(x=160,y = 130)
    r2.place(x=160,y = 150)
    r3.place(x=160,y = 170)
    botaoBuscarAno = Button(windowTwo, text="Buscar Ano", command=buscarPorAno)
    botaoBuscarAno.place(x=250, y=150)
    
    windowTwo.mainloop()


#Gui principal

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

botaoVisualizarAlbuns = Button(window, text="Visualizar Albuns", command=visualizarAlbuns)
botaoVisualizarAlbuns.place(x=210, y=220)

window.mainloop()


