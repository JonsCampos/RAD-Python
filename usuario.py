import tkinter as tk
from tkinter import ttk, messagebox as mb
import classcrud

# Janela
janelaUsuario = tk.Tk()
posx, posy = int((janelaUsuario.winfo_screenwidth()-800)/2), int((janelaUsuario.winfo_screenheight()-500)/2)
janelaUsuario.geometry(f'800x500+{posx}+{posy}')
janelaUsuario.title('Sistema de Controle de acesso')

# Criação das tabelas (caso não exista)
classcrud.tabelas()

# Título
ttk.Label(janelaUsuario, text='Usuários', font=(12)).place(x=367, y=7, width=65)

# Entry - ID Usuário
labelIDUsu = ttk.Label(text='ID do usuário')
labelIDUsu.place(x=60, y=60)
IDUsuario = tk.Entry(janelaUsuario)
IDUsuario.place(x=60, y=80, width=120)

# Entry - Nome usuário
labelNUsuario = ttk.Label(text='Nome de usuário')
labelNUsuario.place(x=240, y=60)
nomeUsuario = tk.Entry(janelaUsuario)
nomeUsuario.place(x=240, y=80, width=120)

# Entry - Senha
labelSenha = ttk.Label(text='Senha')
labelSenha.place(x=420, y=60)
senhaUsuario = tk.Entry(janelaUsuario, show='*')
senhaUsuario.place(x=420, y=80, width=120)

# Entry - ID Funcionário
labelSenha = ttk.Label(text='ID do funcionário')
labelSenha.place(x=600, y=60)
IDFuncionario = tk.Entry(janelaUsuario)
IDFuncionario.place(x=600, y=80, width=120)

# TreeView
colunas = ('ID', 'Nome de usuário', 'Funcionário')            
treeUsuario = ttk.Treeview(janelaUsuario,columns=colunas, selectmode='browse')
treeUsuario['show'] = 'headings'
# Scrollbar
scroll = ttk.Scrollbar(janelaUsuario, orient='vertical', command=treeUsuario.yview)        
scroll.pack(side ='right', fill ='x')
treeUsuario.configure(yscrollcommand=scroll.set)
scroll.place(x=591, y=230, height=225)
# Cabeçalho
treeUsuario.heading('ID', text='ID')
treeUsuario.heading('Nome de usuário', text='Nome de usuário')
treeUsuario.heading('Funcionário', text='Funcionário')
# Colunas
treeUsuario.column('ID',minwidth=0,width=100)
treeUsuario.column('Nome de usuário',minwidth=0,width=140)
treeUsuario.column('Funcionário',minwidth=0,width=140)
treeUsuario.place(x=209, y=230)

# Button - Inserir
inserirbtn = tk.Button(janelaUsuario, text='Inserir', command=lambda: classcrud.insertUsuario(nomeUsuario, senhaUsuario, IDFuncionario , treeUsuario))
inserirbtn.place(x=200, y=140)

# Button - Atualizar
atualizarbtn = tk.Button(janelaUsuario, text='Atualizar', command=lambda: classcrud.updateUsuario(IDUsuario, nomeUsuario, senhaUsuario, treeUsuario))
atualizarbtn.place(x=371.5, y=140)

# Button - Remover
removerbtn = tk.Button(janelaUsuario, text='Remover', command=lambda: classcrud.deleteUsuario(IDUsuario, treeUsuario))
removerbtn.place(x=543, y=140)

# Button - Voltar
inserirbtn = tk.Button(janelaUsuario, text='Voltar', command=lambda: janelaUsuario.destroy())
inserirbtn.place(x=7, y=7)

# Atualização TreeView
classcrud.attTreeUsuario(treeUsuario)

janelaUsuario.mainloop()