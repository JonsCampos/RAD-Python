import sqlite3 as conector

def ins_ent(conexao, cursor):
    id_func = input('Digite o id do funcionário: ')
    id_func = id_func.strip()
    id_local_ent = input('Digite o id do local: ')
    id_local_ent = id_local_ent.strip()
    comando = '''INSERT INTO entrada (funcionario_ID, local_ID) 
	VALUES (?, ?);'''
    cursor.execute(comando, (id_func, id_local_ent))
    confirm = input('Confirmar entrada? [S/N] ')
    if confirm.lower() == 's':
        conexao.commit()
        print('Entrada confirmada!')
    else:
        conexao.rollback()
        print('Entrada cancelada!')

def list_ent(cursor):
    comando = '''SELECT e.entrada_ID, f.nome, s.nome_setor, l.nome_local,  strftime('%d/%m/%Y %H:%M', e.data_hora_ent)
                    FROM Entrada e
                    JOIN Funcionario f ON e.funcionario_ID = f.funcionario_ID
                    JOIN Setor s ON f.setor_ID = s.setor_ID
                    JOIN Local l ON e.local_ID = l.local_ID
                    ORDER BY e.data_hora_ent DESC;'''
    cursor.execute(comando)
    registros = cursor.fetchall()
    print('\nLista de Entradas')
    for registro in registros:
        print(registro)

def ins_sai(conexao, cursor):
    id_func = input('Digite o id do funcionário: ')
    id_func = id_func.strip()
    id_local_sai = input('Digite o id do local: ')
    id_local_sai = id_local_sai.strip()
    comando = '''INSERT INTO saida (funcionario_ID, local_ID) 
	VALUES (?, ?);'''
    cursor.execute(comando, (id_func, id_local_sai))
    confirm = input('Confirmar saída? [S/N] ')
    if confirm.lower() == 's':
        conexao.commit()
        print('Saída confirmada!')
    else:
        conexao.rollback()
        print('Saída cancelada!')

def list_sai(cursor):
    comando = '''SELECT sd.saida_ID, f.nome, st.nome_setor, l.nome_local, strftime('%d/%m/%Y %H:%M', sd.data_hora_sai) 
                    FROM Saida sd
                    JOIN Funcionario f ON sd.funcionario_ID = f.funcionario_ID
                    JOIN Setor st ON f.setor_ID = st.setor_ID
                    JOIN Local l ON sd.local_ID = l.local_ID
                    ORDER BY sd.data_hora_sai DESC;'''
    cursor.execute(comando)
    registros = cursor.fetchall()
    print('\nLista de Saídas')
    for registro in registros:
        print(registro)


conexao = conector.connect("./banco_rad.db") 
cursor = conexao.cursor()

opc = int(input('1 - Inserir Entrada | 2 - Listar Entradas | 3 - Inserir Saída | 4 - Listar Saídas\n'))
if opc == 1:
    ins_ent(conexao, cursor)
elif opc == 2:
    list_ent(cursor)
elif opc == 3:
    ins_sai(conexao, cursor)
elif opc == 4:
    list_sai(cursor)

cursor.close()
conexao.close()
