import tkinter as tk
from tkinter import ttk
import customtkinter as ck
import classcrud

def voltar(janelaAcesso, janelaMenu):
    janelaMenu.deiconify()
    janelaAcesso.destroy()

def acesso(nvl, janelaMenu):
    # Janela
    janelaAcesso = ck.CTkToplevel()
    x, y = 800, 500
    posx, posy = int((janelaAcesso.winfo_screenwidth()-x)/2), int((janelaAcesso.winfo_screenheight()-y)/2)
    janelaAcesso.geometry(f'{x}x{y}+{posx}+{posy}')
    janelaAcesso.resizable(False, False)
    janelaAcesso.after(200, lambda: janelaAcesso.iconbitmap('icon.ico'))
    janelaAcesso.title('Sistema de Controle de acesso')
    janelaMenu.withdraw()
    janelaAcesso.protocol('WM_DELETE_WINDOW', lambda: voltar(janelaAcesso, janelaMenu))

    # Título
    ck.CTkLabel(janelaAcesso, text='Controle de Acesso', font=ck.CTkFont(size=15)).place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    # Usuário
    ck.CTkLabel(janelaAcesso, text=nvl[0], font=ck.CTkFont(size=15)).place(relx=0.92, rely=0.05, anchor=tk.CENTER)

    # Entry - ID Funcionário
    labelFunc = ck.CTkLabel(janelaAcesso, text='ID do funcionário')
    labelFunc.place(relx=0.25, rely=0.16, anchor=tk.CENTER)
    IDFunc = ck.CTkEntry(janelaAcesso)
    IDFunc.place(relx=0.25, rely=0.21, anchor=tk.CENTER)

    # Combobox - Local
    labelLocal = ck.CTkLabel(janelaAcesso, text='Local')
    labelLocal.place(relx=0.5, rely=0.16, anchor=tk.CENTER)
    registros = classcrud.fillComboboxLocal(janelaAcesso)
    local = ck.CTkComboBox(janelaAcesso, 
    values=['Sem registros'] if registros == [] else [registro[0] for registro in registros],
    state='readonly')
    local.set('Selecione...')
    local.place(relx=0.5, rely=0.21, anchor=tk.CENTER)

    # Radiobutton - Tipo
    labelAcesso = ck.CTkLabel(janelaAcesso, text='Tipo de acesso')
    labelAcesso.place(relx=0.75, rely=0.16, anchor=tk.CENTER)
    tipo = tk.StringVar(janelaAcesso, value='Entrada')
    rb1 = ck.CTkRadioButton(janelaAcesso, text='Entrada', variable=tipo, value='Entrada', border_width_checked=4)
    rb1.place(relx=0.75, rely=0.21, anchor=tk.CENTER)
    rb2 = ck.CTkRadioButton(janelaAcesso, text='Saída', variable=tipo, value='Saída', border_width_checked=4)
    rb2.place(relx=0.75, rely=0.26, anchor=tk.CENTER)

    # Estilo TreeView
    style = ttk.Style()
    style.theme_use('default')
    style.configure('estilo.Treeview.Heading', background='#565b5e', foreground='White',fieldbackground='silver', padding=3)
    style.configure('estilo.Treeview', background='#242424', foreground='White',fieldbackground='#242424')
    style.map('estilo.Treeview.Heading', foreground=[('active','Black')])
    style.map('estilo.Treeview', background=[('selected','#1f6aa5')], foreground=[('selected','white')])
    # TreeView
    colunas = ('Nome', 'Setor', 'Tipo', 'Local', 'Data - Hora')            
    treeAcessos = ttk.Treeview(janelaAcesso, columns=colunas, selectmode='browse', style='estilo.Treeview')
    treeAcessos['show'] = 'headings'
    # Scrollbar
    scroll = ck.CTkScrollbar(janelaAcesso, orientation='vertical', command=treeAcessos.yview, height=224)        
    scroll.pack(side ='right', fill ='x')
    treeAcessos.configure(yscrollcommand=scroll.set)
    scroll.place(relx=0.955, rely=0.7, anchor=tk.CENTER)
    # Cabeçalho
    treeAcessos.heading('Nome', text='Nome')
    treeAcessos.heading('Setor', text='Setor')
    treeAcessos.heading('Tipo', text='Tipo')
    treeAcessos.heading('Local', text='Local') 
    treeAcessos.heading('Data - Hora', text='Data - Hora')  
    # Colunas
    treeAcessos.column('Nome',minwidth=0,width=140, anchor=tk.CENTER)
    treeAcessos.column('Setor',minwidth=0,width=140, anchor=tk.CENTER)
    treeAcessos.column('Tipo',minwidth=0,width=140, anchor=tk.CENTER)
    treeAcessos.column('Local',minwidth=0,width=140, anchor=tk.CENTER)
    treeAcessos.column('Data - Hora',minwidth=0,width=150, anchor=tk.CENTER)
    treeAcessos.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    # Button - Inserir
    inserirbtn = ck.CTkButton(janelaAcesso, text='Inserir', command=lambda: classcrud.insertAcesso(IDFunc, local, tipo, treeAcessos, janelaAcesso))
    inserirbtn.place(relx=0.25, rely=0.33, anchor=tk.CENTER)

    # Button - Voltar
    voltarbtn = ck.CTkButton(janelaAcesso, width=50, text='Voltar', command=lambda: voltar(janelaAcesso, janelaMenu))
    voltarbtn.place(relx=0.05, rely=0.05, anchor=tk.CENTER)

    # Atualização TreeView
    classcrud.attTreeAcesso(treeAcessos, janelaAcesso)

    janelaAcesso.mainloop()
