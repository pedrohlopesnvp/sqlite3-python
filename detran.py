import sqlite3

# Função para criar a tabela
def criar_tabela():
    conexao = sqlite3.connect('detran.db') 
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS detran (
                        id INTEGER PRIMARY KEY,
                        placa TEXT NOT NULL,
                        veiculo TEXT NOT NULL,
                        ano INTEGER not null,
                        preco FLOAT,
                        proprietario TEXT,
                        fone TEXT)''')
                        
    conexao.commit()
    conexao.close()

# Função para adicionar um novo carro
def adicionar_carro(placa, veiculo, ano, preco, proprietario, fone):
    conexao = sqlite3.connect('detran.db') 
    cursor = conexao.cursor()

    cursor.execute('''INSERT INTO detran (placa, veiculo, ano, preco, proprietario, fone) VALUES (?, ?, ?, ?, ?, ?)''', (placa, veiculo, ano, preco, proprietario, fone))
    conexao.commit()
    conexao.close()

# Função para listar todos os carros
def listar_carros():
    conexao = sqlite3.connect('detran.db') 
    cursor = conexao.cursor()

    cursor.execute('''SELECT * FROM detran''')
    detrans = cursor.fetchall()

    for detran in detrans:
        print(detran)

    conexao.close()

# Função para atualizar os dados de um carro
def atualiza_carro(id, placa, veiculo, ano, preco, proprietario, fone):
    conexao = sqlite3.connect('detran.db') 
    cursor = conexao.cursor()

    cursor.execute('''UPDATE detran SET placa = ?, veiculo = ?, ano =?, preco = ?, proprietario = ?, fone = ? WHERE id = ?''', (placa, veiculo, ano, preco, proprietario, fone, id))
    conexao.commit()
    conexao.close()

# Função para deletar um carro

def deletar_carro(id):
    conexao = sqlite3.connect('detran.db') 
    cursor = conexao.cursor()

    cursor.execute('''DELETE FROM detran WHERE id = ?''', (id,))
    conexao.commit()
    conexao.close()

# Criar abela (se ela ainda não existir)
criar_tabela()

# Função do menu de escolhas
def menu():
    print("\n 1 - Novo carro \n 2 - Listar carros \n 3 - Atualizar carro \n 4 - Excluir carro \n 5 - Sair \n")

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        placa = input("Digite a placa do carro: ")
        veiculo = input("Digite o veículo: ")
        ano = int(input("Digite o ano do carro: "))
        preco = float(input("Digite o preco do carro: "))
        proprietario = input("Digite o proprietário do carro: ")
        fone = input("Digite o telefone: ")
        adicionar_carro(placa, veiculo, ano, preco, proprietario, fone)
        print("Carro adiciona com sucesso!")
    elif escolha == '2':
        print("\nTodos os carros: ")
        listar_carros()
    elif escolha == '3':
        id = int(input("Digite o id do carro a ser atualizado: "))
        placa = input("Digite a placa do carro: ")
        veiculo = input("Digite o veículo: ")
        ano = int(input("Digite o ano do carro: "))
        preco = float(input("Digite o preco do carro: "))
        proprietario = input("Digite o proprietário do carro: ")
        fone = input("Digite o telefone: ")
        atualiza_carro(id, placa, veiculo, ano, preco, proprietario, fone)
        print("Carro atualizado com sucesso!")
    elif escolha == '4':
        id = int(input("Digite o id do carro que deve ser excluído: "))
        deletar_carro(id)
        print("carro deletado")
    elif escolha == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
