# Inicialmente importar todos itens da biblioteca tkinter o qual sera responsavel pela tela principal o bloco e notas
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename  # importando dois objetos da biblioteca c a funcionalidade de salvar e abrir arquivos

# Construindo nosso bloco de notas atraves da classe que comportara toda a estrutura de codigo
class BlocoPy:
    def __init__(self):
        # Definindo a janela inicial do bloco de notas
        self.janela = Tk()
        # Definindo o titulo do bloco de notas
        self.janela.title("Bloco de Notas Python")
        #Criando uma barra de rolagem
        barra_rolagem = Scrollbar(self.janela) # adiciono a funcionalidade Scrollbar e a janela do bloco como parâmetro e guardo dentro de uma variavel
        barra_rolagem.pack(side=RIGHT, fill=Y) # posiciono a barra de rolagem definindo o lado e o eixo
        # Criando o menu do bloco de notas
        menu_bloco = Menu(self.janela)
        menu_arquivo = Menu(menu_bloco)
        menu_arquivo.add_command(label="Salvar", command=self.salvar)

        menu_arquivo.add_command(label="Abrir", command=self.abrir)

        menu_bloco.add_cascade(label="Arquivo", menu=menu_arquivo)

        menu_ajuda = Menu(menu_bloco)
        menu_ajuda.add_command(label="Sobre",command=self.sobre)

        menu_bloco.add_cascade(label="Ajuda", menu=menu_ajuda)
        self.janela.config(menu=menu_bloco)
        self.janela.mainloop()

BlocoPy()