import tkinter as tk
from tkinter import ttk
import customtkinter as ck
import classcrud

# Janela
janelaMain = ck.CTk()
x, y = 800, 500
posx, posy = int((janelaMain.winfo_screenwidth()-x)/2), int((janelaMain.winfo_screenheight()-y)/2)
janelaMain.geometry(f'{x}x{y}+{posx}+{posy}')
janelaMain.resizable(False, False)
janelaMain.iconbitmap('icon.ico')
janelaMain.title('Sistema de Controle de acesso')

# Criação das tabelas (caso não exista)
classcrud.tabelas()

# Título
ck.CTkLabel(janelaMain, text='Login', font=ck.CTkFont(size=15)).place(relx=0.5, rely=0.05, anchor=tk.CENTER)

# Imagem
#icon = tk.PhotoImage(file='loginIcon.png')
#label = ck.CTkLabel(janelaMain, image=icon)
#label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

# Entry - Usuário
labelLgnUsuario = ck.CTkLabel(janelaMain, text='Usuário')
labelLgnUsuario.place(relx=0.40, rely=0.53, anchor=tk.CENTER)
lgnUsuario = ck.CTkEntry(janelaMain)
lgnUsuario.place(relx=0.52, rely=0.53, anchor=tk.CENTER)

# Entry - Senha
labelLgnSenha = ck.CTkLabel(janelaMain, text='Senha')
labelLgnSenha.place(relx=0.40, rely=0.61, anchor=tk.CENTER)
lgnSenha = ck.CTkEntry(janelaMain, show='*')
lgnSenha.place(relx=0.52, rely=0.61, anchor=tk.CENTER)

# Button - Entrar
entrarbtn = ck.CTkButton(janelaMain, text='Entrar', command=lambda: classcrud.entrar(lgnUsuario, lgnSenha, janelaMain))
entrarbtn.place(relx=0.5, rely=0.73, anchor=tk.CENTER)

janelaMain.mainloop()
