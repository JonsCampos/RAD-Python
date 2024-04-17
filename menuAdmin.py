import tkinter as tk
from tkinter import ttk
import classcrud
import acesso
import setor
import funcionario
import usuario
import local

def menuAdmin(nvl):
    # Janela
    janelaMenuAdmin = tk.Toplevel()
    x, y = 800, 500
    posx, posy = int((janelaMenuAdmin.winfo_screenwidth()-x)/2), int((janelaMenuAdmin.winfo_screenheight()-y)/2)
    janelaMenuAdmin.geometry(f'{x}x{y}+{posx}+{posy}')
    janelaMenuAdmin.resizable(False, False)
    janelaMenuAdmin.iconbitmap('icon.ico')
    janelaMenuAdmin.title('Sistema de Controle de acesso')

    # Título
    ttk.Label(janelaMenuAdmin, text='Menu', font=(12)).place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    # Usuário
    ttk.Label(janelaMenuAdmin, text=nvl[0], font=(12)).place(relx=0.92, rely=0.05, anchor=tk.CENTER)

    # Button - Acesso
    acessobtn = tk.Button(janelaMenuAdmin, text='Acesso', command=lambda: acesso.acesso(nvl))
    acessobtn.place(relx=0.5, rely=0.1666, anchor=tk.CENTER)

    # Button - Setor
    setorbtn = tk.Button(janelaMenuAdmin, text='Setor', command=lambda: setor.setor(nvl))
    setorbtn.place(relx=0.5, rely=0.3332, anchor=tk.CENTER)

    # Button - Funcionario
    funcionariobtn = tk.Button(janelaMenuAdmin, text='Funcionário', command=lambda: funcionario.funcionario(nvl))
    funcionariobtn.place(relx=0.5, rely=0.4998, anchor=tk.CENTER)

    # Button - Usuario
    usuariobtn = tk.Button(janelaMenuAdmin, text='Usuário', command=lambda: usuario.usuario(nvl))
    usuariobtn.place(relx=0.5, rely=0.6664, anchor=tk.CENTER)

    # Button - Local
    localbtn = tk.Button(janelaMenuAdmin, text='Local', command=lambda: local.local(nvl))
    localbtn.place(relx=0.5, rely=0.833, anchor=tk.CENTER)

    # Button - Sair
    sairbtn = tk.Button(janelaMenuAdmin, text='Sair', command=janelaMenuAdmin.destroy)
    sairbtn.place(relx=0.05, rely=0.05, anchor=tk.CENTER)

    janelaMenuAdmin.mainloop()