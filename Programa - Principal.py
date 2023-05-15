import tkinter as tk
import pyodbc 

# Criando Janela:
janela = tk.Tk()
janela.title('Cadastro de Fornecedor')
janela.geometry("800x900")
janela.configure(bg="white")

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-FFAT61K\SQLEXPRESS;"
    "Database=Ads_Material;"
)
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

print('Conexão com sucesso!!')

def atualizar_fornecedor():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    

    comando = f"""UPDATE Fornecedores
         set telefone = '{telefone}'
         where nome  = '{nome}'
        """

    cursor.execute(comando)
    cursor.commit()
    print('Fornecedor Atualizado com Sucesso!!')

def cadastrar_produto(idFornecedor, produto, categoria, lote):

    # Inserção do produto relacionado ao fornecedor na tabela "produto"
    comando = f"""INSERT INTO Produtos (IdFornecedor, Produto, Categoria, Lote) VALUES ({idFornecedor}, '{produto}', '{categoria}', {lote})"""
    cursor.execute(comando)
    cursor.commit()


def cadastrar_fornecedor():
   
    id   = int(entry_id.get())
    nome = entry_nome.get()
    cidade = entry_cidade.get()
    bairro = entry_bairro.get()
    endereco = entry_ende.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    cnpj = entry_cnpj.get()
    produto = entry_produto.get()
    categoria = entry_categoria.get()
    lote = int(entry_lote.get())

    comando = f"""INSERT INTO Fornecedores (IdFornecedor,Nome, Cidade, Bairro, Endereço, Telefone, Email, cnpj, Produto, Categoria, Lote)
        VALUES ({id},'{nome}','{cidade}','{bairro}','{endereco}','{telefone}','{email}', '{cnpj}', '{produto}','{categoria}', {lote})"""

    cursor.execute(comando)
    cursor.commit()

    cadastrar_produto(id, produto, categoria, lote)
   ## print('Cadastro Realizado com Sucesso!!')



def  consultar_fornecedor():
    nome = entry_nome.get()

    comando = f""" SELECT * FROM Fornecedores
                   WHERE Fornecedores.nome = '{nome}';
                   """

    cursor.execute(comando)


    for linha in cursor.fetchall():
        texto= f"Produto:{linha[8]} \n"
        caixa_texto.insert("1.0", texto)
    


                        

def deletar_produto(idFornecedor):

    # Inserção do produto relacionado ao fornecedor na tabela "produto"
    comando = f""" DELETE FROM Produtos
         where idFornecedor = '{idFornecedor}'
        """

    cursor.execute(comando)
    cursor.commit()


def  deletar_fornecedor():
    id = entry_id.get()

    comando = f""" DELETE FROM Fornecedores
         where idFornecedor = '{id}'
        """

    cursor.execute(comando)
    cursor.commit()

    deletar_produto(id)
    
    print('Dados de fornecedor excluido!!')


entry_id = tk.Entry(janela, width=35, bd=2)
entry_id.grid(row=0, column=1, padx=0, pady=0)

entry_nome = tk.Entry(janela, width=35, bd=2)
entry_nome.grid(row=1, column=1, padx=0, pady=0)

entry_cidade = tk.Entry(janela, width=35, bd=2)
entry_cidade.grid(row=2, column=1, padx=10, pady=10)

entry_bairro = tk.Entry(janela, width=35, bd=2)
entry_bairro.grid(row=3, column=1, padx=10, pady=10)

entry_ende = tk.Entry(janela, width=35, bd=2)
entry_ende.grid(row=4, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, width=35, bd=2)
entry_telefone.grid(row=5, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, width=35, bd=2)
entry_email.grid(row=6, column=1, padx=10, pady=10)

entry_cnpj = tk.Entry(janela, width=35, bd=2)
entry_cnpj.grid(row=7, column=1, padx=10, pady=10)

entry_produto = tk.Entry(janela, width=35, bd=2)
entry_produto.grid(row=8, column=1, padx=10, pady=10)

entry_categoria = tk.Entry(janela, width =35, bd=2)
entry_categoria.grid(row=9,column=1, padx=10, pady=10)

entry_lote= tk.Entry(janela, width =35, bd=2)
entry_lote.grid(row=10,column=1, padx=10, pady=10)



#Titulo Entradas:

label_id = tk.Label(janela, text='id',justify="left", )
label_id.grid(row=0,column=0, padx=5, pady=2, sticky="W", columnspan=1)

label_nome = tk.Label(janela, text='Nome',justify="left", )
label_nome.grid(row=1,column=0, padx=5, pady=2, sticky="W", columnspan=1)


label_cidade = tk.Label(janela, text='Cidade', justify="left")
label_cidade.grid(row=2, column=0, padx=5, pady=2, sticky="W", columnspan=1)

label_bairro = tk.Label(janela, text='Bairro', justify="left")
label_bairro.grid(row=3, column=0 , padx=5, pady=2, sticky="W", columnspan=1)


label_ende = tk.Label(janela, text='Endereço', justify="left")
label_ende.grid(row=4, column=0, padx=5, pady=2, sticky="W",columnspan=1)

label_telefone = tk.Label(janela, text='Telefone', justify="left")
label_telefone.grid(row=5,column=0, padx=5, pady=2, sticky="W", columnspan=1)

label_email = tk.Label(janela, text='Email', justify="left")
label_email.grid(row=6,column=0, padx=5, pady=2, sticky="W", columnspan=1)

label_cnpj = tk.Label(janela, text='CNPJ',justify="left")
label_cnpj.grid(row=7,column=0, padx=5, pady=2, sticky="W", columnspan=1)

label_Produto = tk.Label(janela, text='Produto', justify="left")
label_Produto.grid(row=8,column=0, padx=5, pady=2, sticky="W", columnspan=1)

label_categoria = tk.Label(janela, text='Categoria', justify="left")
label_categoria.grid(row=9,column=0, padx=5, pady=2, sticky="W", columnspan=1)

label_lote= tk.Label(janela, text='Lote', justify="left")
label_lote.grid(row=10,column=0, padx=5, pady=2, sticky="W", columnspan=1)


botao_cadastrar = tk.Button(text='Cadastrar Fornecedor', command=cadastrar_fornecedor)
botao_cadastrar.grid(row=11, column=1,columnspan=1, padx=10, pady=10 , ipadx =5, sticky="nswe")

botao_Atualiza = tk.Button(text='Atualizar Fornecedor', command=atualizar_fornecedor)
botao_Atualiza.grid(row=12, column=1,columnspan=1, padx=10, pady=10 , ipadx =5, sticky="nswe")

botao_delete = tk.Button(text='Delete Fornecedor', command=deletar_fornecedor)
botao_delete.grid(row=13, column=1,columnspan=1, padx=10, pady=10 , ipadx =5, sticky="nswe")

botao_consulta = tk.Button(text='Consultar Fornecedor', command=consultar_fornecedor)
botao_consulta.grid(row=14, column=1,columnspan=1, padx=10, pady=10 , ipadx =5, sticky="nswe")

caixa_texto = tk.Text(janela, height=15, width=85, bd=2)
caixa_texto.grid(row=15, column=1)



janela.mainloop()
