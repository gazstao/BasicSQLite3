#Sqlite3 2019-12-01 12h50 Gazstao (h)

import sqlite3

print ("\nSQLite3 Gazstao 2019 (h)2")

def create_table():
    print("Criando tabelas, se não existirem...")
    conn = sqlite3.connect("gazstao.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantidade INTEGER, preco REAL)")
    conn.commit()
    conn.close()

def insert(item, quantidade, preco):
    conn = sqlite3.connect("gazstao.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item, quantidade,preco))
    conn.commit()
    conn.close()
   
def view():
    try:
        conn = sqlite3.connect("gazstao.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM store")
        linhas = cur.fetchall()
        conn.close()
        return linhas
    except: 
        return ["Tabela não existe ou vazia!"]

create_table()
while (True):
    print ("\n1) Cadastrar Produto")
    print ("2) Ver Produtos Cadastrados")
    print ("9) Sair")
    i = input ("Digite uma opção: ")
    if i == "1":
        item = input("Nome do Item: ")
        quantidade = input("Quantidade Disponivel: ")
        preco = input("Preco do Produto: ")
        insert(item,quantidade, preco)
    elif i == "2":
        for item in view():
            print(item)
    elif i == "9":
        print("\nObrigado!")
        break
    else:
         print("Opcao invalida!")