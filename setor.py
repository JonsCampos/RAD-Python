import tkinter as tk
from tkinter import ttk, messagebox as mb
import classcrud

# Janela
janelaSetor = tk.Tk()
posx, posy = int((janelaSetor.winfo_screenwidth()-800)/2), int((janelaSetor.winfo_screenheight()-500)/2)
janelaSetor.geometry(f'800x500+{posx}+{posy}')
janelaSetor.title('Sistema de Controle de acesso')

# Criação das tabelas (caso não exista)
classcrud.tabelas()

# Título
ttk.Label(janelaSetor, text='Setores', font=(12)).place(x=370, y=7, width=60)

# Entry - ID do local
labelIDSetor = ttk.Label(text='ID do setor')
labelIDSetor.place(x=200, y=60)
IDSetor = tk.Entry(janelaSetor)
IDSetor.place(x=200, y=80, width=120)

# Entry - Nome do local
labelNSetor = ttk.Label(text='Nome do setor')
labelNSetor.place(x=480, y=60)
nomeSetor = tk.Entry(janelaSetor)
nomeSetor.place(x=480, y=80, width=120)

# TreeView
colunas = ('ID', 'Nome')
treeSetor = ttk.Treeview(janelaSetor,columns=colunas, selectmode='browse')
treeSetor['show'] = 'headings'
# Scrollbar
scroll = ttk.Scrollbar(janelaSetor, orient='vertical', command=treeSetor.yview)        
scroll.pack(side ='right', fill ='x')
treeSetor.configure(yscrollcommand=scroll.set)
scroll.place(x=542, y=230, height=225)
# Cabeçalho
treeSetor.heading('ID', text='ID')
treeSetor.heading('Nome', text='Nome')
# Colunas
treeSetor.column('ID',minwidth=0,width=140)
treeSetor.column('Nome',minwidth=0,width=140)
treeSetor.place(x=260, y=230)

# Button - Inserir
inserirbtn = tk.Button(janelaSetor, text='Inserir', command=lambda: classcrud.insertSetor(nomeSetor, treeSetor))
inserirbtn.place(x=200, y=140)

# Button - Atualizar
atualizarbtn = tk.Button(janelaSetor, text='Atualizar', command=lambda: classcrud.updateSetor(IDSetor, nomeSetor, treeSetor))
atualizarbtn.place(x=371.5, y=140)

# Button - Remover
removerbtn = tk.Button(janelaSetor, text='Remover', command=lambda: classcrud.deleteSetor(IDSetor, treeSetor))
removerbtn.place(x=543, y=140)

# Button - Voltar
inserirbtn = tk.Button(janelaSetor, text='Voltar', command=lambda: janelaSetor.destroy())
inserirbtn.place(x=7, y=7)

# Atualização TreeView
classcrud.attTreeSetor(treeSetor)

janelaSetor.mainloop()
