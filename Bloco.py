# Inicialmente importar todos itens da biblioteca tkinter o qual sera responsavel pela tela principal o bloco e notas
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename  # importando dois objetos da biblioteca c a funcionalidade de salvar e abrir arquivos

# Construindo nosso bloco de notas atraves da classe que comportará toda a estrutura de codigo
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
        # Criando um campo para escrever varias linhas
        self.text = Text(self.janela) # adicionando a funcionalidade do texto
        self.text.pack(expand=YES, fill=BOTH) # Expandindo e preenchendo a tela
        self.text.config(yscrollcommand=barra_rolagem.set) # Definindo o comando da barra de rolagemm
        barra_rolagem.config(command=self.text.yview) # Visualização do texto

        self.janela.mainloop() # Responsavel por deixar a janela aberta


    # Funcionalidade responsavel por salvar o bloco de notas
    def salvar(self):
        nome_arquivo = asksaveasfilename() #Funcão responsavel por salvar o arquivo
        try:
            arquivo = open(nome_arquivo, 'w')
            texto_saida = self.text.get(0.0, END)
            arquivo.write(texto_saida)
        except:
            pass
        finally:
            arquivo.close()
    #Função de abrir o arquivo
    def abrir(self):
        nome_arquivo = askopenfilename()
        try:
            arquivo = open(nome_arquivo, 'r')
            conteudo = arquivo.read()
            
            self.text.delete(0.0, END)
            self.text.insert(0.0, conteudo)
        except:
            pass
    #Função "Sobre"
    def sobre(self):
        janela = Tk()

        janela.title("Sobre")

        texto = ("BlocoPy Joelzera: versao 1.0")
        texto_label = Label(janela, text=texto)
        texto_label.pack()

BlocoPy()
        
