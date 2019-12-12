from funcoes import cor_vermelho, cor_verde, cor_ciano, get_programador, get_linguagem, get_framework, get_banco_dados, verifica_dados

# Contratações corretas

# Mateus = framework: angular, linguagem: python, db: mongo
# Tiago = framework: vue, linguagem: java, db: postgree
# Nicole = framework: react, linguagem: php, db: mysqlserver


lista = []


programadores = ['Mateus', 'Tiago', 'Nicole']
bancos_dados = ['MySqlServer', 'PostgreSQL', 'MongoDb']
linguagens = ['Python', 'Java', 'PHP']
frameworks = ['React', 'Vue', 'Angular']


for i in range(3):
    dado = {}
    dado['programador'] = get_programador(programadores)
    dado['framework'] = get_framework(frameworks)
    dado['linguagem'] = get_linguagem(linguagens)
    dado['banco_dados'] = get_banco_dados(bancos_dados)
    lista.append(dado)


for i in lista:
    print(f"{'-'*20}\n")    
    print(cor_ciano(f"Nome: {i['programador']}, Linguagem: {i['linguagem']}, Framework {i['framework']}, Banco de dados: {i['banco_dados']}\n"))


if verifica_dados(lista):
    print(f"{'-'*20}\n")
    print(f"{cor_verde('Contratados nas Squads!')}\n")
    print(f"{'-'*20}\n")
else:
    print(f"{'-'*20}\n")
    print(f"{cor_vermelho('Seus conhecimentos não combinam com as necessidades das Squads!')}\n")
    print(f"{'-'*20}\n")                 