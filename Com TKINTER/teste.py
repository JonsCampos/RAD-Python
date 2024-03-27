import tkinter as tk
from tkinter import ttk
import crudTeste

# Janela
janela = tk.Tk()
janela.geometry('800x500')
janela.title('Controle de acesso')

#Título
ttk.Label(janela, text="Sistema de Controle de Acesso", font=(12)).place(x=285, y=7)

# Entry - ID Funcionário
labelFunc = ttk.Label(text='ID do funcionário')
labelFunc.place(x=100, y=60)
idFunc = tk.Entry(janela)
idFunc.place(x=100, y=80)

# Combobox - Portaria
labelPortaria = ttk.Label(text='Portaria')
labelPortaria.place(x=320, y=60)
portaria = ttk.Combobox(janela, state='readonly')
registros = crudTeste.fillCombobox()
portaria['values'] = [registro[0] for registro in registros]
portaria.current(0)
portaria.place(x=320, y=80)

# Radiobutton - Tipo
labelAcesso = ttk.Label(text='Tipo de acesso')
labelAcesso.place(x=570, y=60)
tipo = tk.StringVar(value='Entrada')
rb1 = tk.Radiobutton(janela, text='Entrada', variable=tipo, value='Entrada')
rb1.place(x=570, y=80)
rb2 = tk.Radiobutton(janela, text='Saída', variable=tipo, value='Saída')
rb2.place(x=570, y=100)

# TreeView
colunas = ('Nome', 'Setor', 'Tipo', 'Portaria', 'Data - Hora')            
treeAcessos = ttk.Treeview(janela,columns=colunas, selectmode='browse')
treeAcessos['show'] = 'headings'
# Scrollbar
scroll = ttk.Scrollbar(janela, orient="vertical", command=treeAcessos.yview)        
scroll.pack(side ='right', fill ='x')
treeAcessos.configure(yscrollcommand=scroll.set)
scroll.place(x=752, y=230, height=225)
# Cabeçalho
treeAcessos.heading('Nome', text='Nome')
treeAcessos.heading('Setor', text='Setor')
treeAcessos.heading('Tipo', text='Tipo')
treeAcessos.heading('Portaria', text='Portaria') 
treeAcessos.heading('Data - Hora', text='Data - Hora')  
# Colunas
treeAcessos.column('Nome',minwidth=0,width=140)
treeAcessos.column('Setor',minwidth=0,width=140)
treeAcessos.column('Tipo',minwidth=0,width=140)
treeAcessos.column('Portaria',minwidth=0,width=140)
treeAcessos.column('Data - Hora',minwidth=0,width=150)
treeAcessos.place(x=40, y=230)

# Button - Inserir
inserirbtn = tk.Button(janela, text='Inserir', command=lambda: crudTeste.insert(idFunc, portaria, tipo, treeAcessos))
inserirbtn.place(x=100, y=140)

# Atualização TreeView
crudTeste.attTree(treeAcessos)

janela.mainloop()