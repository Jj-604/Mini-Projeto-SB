# tela de inicio
#biblioteca tkinter sendo usado para a criação da interface gráfica
from tkinter import * 
#codigo para criar a janela principal
Jenela = Tk()
Jenela.title("Tela Inicial")
Jenela.geometry("400x300")
Inomrações_iniciais = Label(Jenela, text="Deseja cadastrar um novo usuario ou fazer login?")
Inomrações_iniciais.grid(column=0, row=0)
#botão para cadastrar novo usuario
def cadastrar_usuario():
    Jenela.destroy()
    import tela_cadastro
botao_cadastrar = Button(Jenela, text="Cadastrar Novo Usuario", command=cadastrar_usuario)
botao_cadastrar.grid(column=0, row=1)
#botão para fazer login




#codigo para manter a janela aberta
Jenela.mainloop()