import sqlite3 as conector
from tkinter import messagebox as mb
import classes

def fillCombobox():
    try:
        # Select - Locais
        conexao = conector.connect('./Banco/db_controle_acesso.db') 
        cursor = conexao.cursor()
        comando = '''SELECT nome_local FROM Local;'''
        cursor.execute(comando)
        registros = cursor.fetchall()

    except conector.Error as erro:
            mb.showerror("Erro", f'Erro ao conectar-se ao banco de dados: {erro}')
    finally:
        if (conexao):
            cursor.close()
            conexao.close()
    return registros

def verificarFunc(idFunc, cursor):
    # Select - Quantidade Funcionário
    cursor.execute('SELECT COUNT(*) FROM funcionario WHERE funcionario_ID = ?', (idFunc, ))
    selectFunc = cursor.fetchone()[0]
    return selectFunc

def insert(idFunc, portaria, tipo, treeAcessos):
    try:
        conexao = conector.connect('./Banco/db_controle_acesso.db') 
        cursor = conexao.cursor()

        # Verificação Funcionário
        selectFunc = verificarFunc(idFunc.get(), cursor)
        if selectFunc == 0:
            mb.showerror("Erro", "Funcionário não encontrado")
            return

        # instância da classe Acesso
        acesso = classes.Acesso(idFunc.get(), portaria.current()+1, tipo.get())

        # Insert - Acesso
        comando = '''INSERT INTO acesso (funcionario_ID, local_ID, tipo) 
        VALUES (?, ?, ?);'''
        cursor.execute(comando, (acesso.id_func, acesso.id_local, acesso.tipo))

        # Messagebox - Confirmação
        if mb.askyesno('Confirmação', 'Confirmar acesso?'):
            conexao.commit()
        else:
            conexao.rollback()
            
    except conector.Error as erro:
            mb.showerror("Erro", f'Erro ao conectar-se ao banco de dados: {erro}')
    finally:
        if (conexao):
            cursor.close()
            conexao.close()

    # Atualização TreeView
    attTree(treeAcessos)

def attTree(treeAcessos):
    # Apagar registros antigos
    for registro in treeAcessos.get_children():
        treeAcessos.delete(registro)

    try:
        # Select - Acessos
        conexao = conector.connect('./Banco/db_controle_acesso.db') 
        cursor = conexao.cursor()
        comando = '''SELECT f.nome, s.nome_setor, a.tipo, l.nome_local,  strftime('%d/%m/%Y - %H:%M', a.data_hora)
                    FROM Acesso a
                    JOIN Funcionario f ON a.funcionario_ID = f.funcionario_ID
                    JOIN Setor s ON f.setor_ID = s.setor_ID
                    JOIN Local l ON a.local_ID = l.local_ID
                    ORDER BY a.data_hora DESC;'''
        cursor.execute(comando)
        registros = cursor.fetchall()

        # Colocar novos registros
        for registro in registros:
            treeNome = registro[0]
            treeSetor = registro[1]
            treeTipo = registro[2]
            treePortaria = registro[3]
            treeDt_hr = registro[4]
            treeAcessos.insert('', 'end', values=(treeNome, treeSetor, treeTipo, treePortaria, treeDt_hr))
            
    except conector.Error as erro:
            mb.showerror("Erro", f'Erro ao conectar-se ao banco de dados: {erro}')
    finally:
        if (conexao):
            cursor.close()
            conexao.close()
