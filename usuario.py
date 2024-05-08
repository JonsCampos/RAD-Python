import tkinter as tk
from tkinter import ttk
import customtkinter as ck
import classcrud

def voltar(janelaUsuario, janelaMenu):
    janelaMenu.deiconify()
    janelaUsuario.destroy()

def usuario(nvl, janelaMenu):
    # Janela
    janelaUsuario = ck.CTkToplevel()
    x, y = 800, 500
    posx, posy = int((janelaUsuario.winfo_screenwidth()-x)/2), int((janelaUsuario.winfo_screenheight()-y)/2)
    janelaUsuario.geometry(f'{x}x{y}+{posx}+{posy}')
    janelaUsuario.resizable(False, False)
    janelaUsuario.after(200, lambda: janelaUsuario.iconbitmap('icon.ico'))
    janelaUsuario.title('Sistema de Controle de acesso')
    janelaMenu.withdraw()
    janelaUsuario.protocol("WM_DELETE_WINDOW", lambda: voltar(janelaUsuario, janelaMenu))

    # Título
    ck.CTkLabel(janelaUsuario, text='Usuários', font=ck.CTkFont(size=15)).place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    # Usuário
    ck.CTkLabel(janelaUsuario, text=nvl[0], font=ck.CTkFont(size=15)).place(relx=0.92, rely=0.05, anchor=tk.CENTER)

    # Entry - ID Usuário
    labelIDUsu = ck.CTkLabel(janelaUsuario, text='ID do usuário')
    labelIDUsu.place(relx=0.2, rely=0.16, anchor=tk.CENTER)
    IDUsuario = ck.CTkEntry(janelaUsuario)
    IDUsuario.place(relx=0.2, rely=0.21, anchor=tk.CENTER)

    # Entry - Nome usuário
    labelNUsuario = ck.CTkLabel(janelaUsuario, text='Nome de usuário')
    labelNUsuario.place(relx=0.4, rely=0.16, anchor=tk.CENTER)
    nomeUsuario = ck.CTkEntry(janelaUsuario)
    nomeUsuario.place(relx=0.4, rely=0.21, anchor=tk.CENTER)

    # Entry - Senha
    labelSenha = ck.CTkLabel(janelaUsuario, text='Senha')
    labelSenha.place(relx=0.6, rely=0.16, anchor=tk.CENTER)
    senhaUsuario = ck.CTkEntry(janelaUsuario, show='*')
    senhaUsuario.place(relx=0.6, rely=0.21, anchor=tk.CENTER)

    # Entry - ID Funcionário
    labelSenha = ck.CTkLabel(janelaUsuario, text='ID do funcionário')
    labelSenha.place(relx=0.8, rely=0.16, anchor=tk.CENTER)
    IDFuncionario = ck.CTkEntry(janelaUsuario)
    IDFuncionario.place(relx=0.8, rely=0.21, anchor=tk.CENTER)

    # Estilo TreeView
    style = ttk.Style()
    style.theme_use('default')
    style.configure('estilo.Treeview.Heading', background='#565b5e', foreground='White',fieldbackground='silver', padding=3)
    style.configure('estilo.Treeview', background='#242424', foreground='White',fieldbackground='#242424')
    style.map('estilo.Treeview.Heading', foreground=[('active','Black')])
    style.map('estilo.Treeview', background=[('selected','#1f6aa5')], foreground=[('selected','white')])
    # TreeView
    colunas = ('ID', 'Nome de usuário', 'Funcionário')            
    treeUsuario = ttk.Treeview(janelaUsuario, columns=colunas, selectmode='browse', style='estilo.Treeview')
    treeUsuario['show'] = 'headings'
    # Scrollbar
    scroll = ck.CTkScrollbar(janelaUsuario, orientation='vertical', command=treeUsuario.yview, height=224)
    scroll.pack(side ='right', fill ='x')
    treeUsuario.configure(yscrollcommand=scroll.set)
    scroll.place(relx=0.749, rely=0.7, anchor=tk.CENTER)
    # Cabeçalho
    treeUsuario.heading('ID', text='ID')
    treeUsuario.heading('Nome de usuário', text='Nome de usuário')
    treeUsuario.heading('Funcionário', text='Funcionário')
    # Colunas
    treeUsuario.column('ID',minwidth=0,width=100, anchor=tk.CENTER)
    treeUsuario.column('Nome de usuário',minwidth=0,width=140, anchor=tk.CENTER)
    treeUsuario.column('Funcionário',minwidth=0,width=140, anchor=tk.CENTER)
    treeUsuario.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    # Selecionar
    def selecionarRegistros(event):
        IDUsuario.delete(0, tk.END)
        nomeUsuario.delete(0, tk.END)
        IDFuncionario.delete(0, tk.END)

        for selecao in treeUsuario.selection():  
            item = treeUsuario.item(selecao)  
            idusu, nomeusu = item["values"][0:2]  
            IDUsuario.insert(0, idusu)  
            nomeUsuario.insert(0, nomeusu)
            idfunc = classcrud.registroIDFunc(nomeusu, janelaUsuario)
            IDFuncionario.insert(0, idfunc)

    treeUsuario.bind("<<TreeviewSelect>>", selecionarRegistros)

    # Button - Inserir
    inserirbtn = ck.CTkButton(janelaUsuario, text='Inserir', command=lambda: classcrud.insertUsuario(nomeUsuario, senhaUsuario, IDFuncionario , treeUsuario, janelaUsuario))
    inserirbtn.place(relx=0.25, rely=0.33, anchor=tk.CENTER)

    # Button - Atualizar
    atualizarbtn = ck.CTkButton(janelaUsuario, text='Atualizar', command=lambda: classcrud.updateUsuario(IDUsuario, nomeUsuario, senhaUsuario, treeUsuario, janelaUsuario))
    atualizarbtn.place(relx=0.50, rely=0.33, anchor=tk.CENTER)

    # Button - Remover
    removerbtn = ck.CTkButton(janelaUsuario, text='Remover', command=lambda: classcrud.deleteUsuario(IDUsuario, treeUsuario, janelaUsuario))
    removerbtn.place(relx=0.75, rely=0.33, anchor=tk.CENTER)

    # Button - Voltar
    inserirbtn = ck.CTkButton(janelaUsuario, width=50, text='Voltar', command=lambda: voltar(janelaUsuario, janelaMenu))
    inserirbtn.place(relx=0.05, rely=0.05, anchor=tk.CENTER)

    # Atualização TreeView
    classcrud.attTreeUsuario(treeUsuario, janelaUsuario)

    janelaUsuario.mainloop()
