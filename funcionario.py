import tkinter as tk
from tkinter import ttk, messagebox as mb
import classcrud

# Janela
janelaFuncionario = tk.Tk()
posx, posy = int((janelaFuncionario.winfo_screenwidth()-800)/2), int((janelaFuncionario.winfo_screenheight()-500)/2)
janelaFuncionario.geometry(f'800x500+{posx}+{posy}')
janelaFuncionario.title('Sistema de Controle de acesso')

# Criação das tabelas (caso não exista)
classcrud.tabelas()

# Título
ttk.Label(janelaFuncionario, text='Funcionários', font=(12)).place(x=349, y=7, width=100)

# Entry - ID do funcionário
labelIDF = ttk.Label(text='ID do Funcionário')
labelIDF.place(x=180, y=60)
IDFuncionario = tk.Entry(janelaFuncionario)
IDFuncionario.place(x=180, y=80, width=120)

# Entry - Nome do funcionário
labelNFuncionario = ttk.Label(text='Nome do Funcionário')
labelNFuncionario.place(x=340, y=60)
nomeFuncionario = tk.Entry(janelaFuncionario)
nomeFuncionario.place(x=340, y=80, width=120)

# Entry - ComboBox do funcionário
labelSFuncionario = ttk.Label(text='Setor do Funcionário')
labelSFuncionario.place(x=500, y=60)
setorFuncionario = ttk.Combobox(janelaFuncionario, state='readonly')
setorFuncionario.place(x=500, y=80, width=120)

registros = classcrud.fillComboboxSetor()
if registros == []:
    setorFuncionario['values'] = ['Sem registros']
else:
    setorFuncionario['values'] = [registro[0] for registro in registros]
setorFuncionario.current(0)

# TreeView
colunas = ('ID', 'Nome', 'Setor')            
treeFuncionario = ttk.Treeview(janelaFuncionario,columns=colunas, selectmode='browse')
treeFuncionario['show'] = 'headings'

# Scrollbar
scroll = ttk.Scrollbar(janelaFuncionario, orient='vertical', command=treeFuncionario.yview)        
scroll.pack(side ='right', fill ='x')
treeFuncionario.configure(yscrollcommand=scroll.set)
scroll.place(x=612, y=230, height=225)

# Cabeçalho
treeFuncionario.heading('ID', text='ID')
treeFuncionario.heading('Nome', text='Nome')
treeFuncionario.heading ('Setor', text='Setor')

# Colunas
treeFuncionario.column('ID',minwidth=0,width=140)
treeFuncionario.column('Nome',minwidth=0,width=140)
treeFuncionario.column('Setor',minwidth=0,width=140)
treeFuncionario.place(x=190, y=230)

# Button - Inserir
inserirbtn = tk.Button(janelaFuncionario, text='Inserir', command=lambda: classcrud.insertFuncionario(nomeFuncionario, treeFuncionario))
inserirbtn.place(x=200, y=140)

# Button - Atualizar
atualizarbtn = tk.Button(janelaFuncionario, text='Atualizar', command=lambda: classcrud.updateFuncionario(IDFuncionario, nomeFuncionario, treeFuncionario))
atualizarbtn.place(x=371.5, y=140)

# Button - Remover
removerbtn = tk.Button(janelaFuncionario, text='Remover', command=lambda: classcrud.deleteFuncionario(IDFuncionario, treeFuncionario))
removerbtn.place(x=543, y=140)

# Button - Voltar
inserirbtn = tk.Button(janelaFuncionario, text='Voltar', command=lambda: janelaFuncionario.destroy())
inserirbtn.place(x=7, y=7)

# Atualização TreeView
classcrud.attTreeFuncionario(treeFuncionario)

janelaFuncionario.mainloop()
