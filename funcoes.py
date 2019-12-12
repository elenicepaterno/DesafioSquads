def cor_vermelho(frase): 
    frase = '\033[31m' + frase + '\033[0;0m'
    return frase


def cor_verde(frase):
    frase = '\033[32m' + frase + '\033[0;0m'
    return frase


def cor_ciano(frase):
    frase = '\033[36m' + frase + '\033[0;0m'
    return frase


def get_inteiro(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except:
            print('Não é um número válido!')
        else:
            return n 


def get_programador(programadores):
    i = 1 
    for programador in programadores:
        print(f'{i} - {programador}')
        i += 1
  
    while True:
        try:
            n = get_inteiro('Escolha um programador: ')
            nome_programador = programadores[n - 1]
        except:
            print('Não existe esse programador!')
        else:
            break

    programadores.remove(nome_programador)
    return nome_programador


def get_linguagem(linguagens):
    i = 1
    for linguagem in linguagens:
        print(f'{i} - {linguagem}')
        i += 1

    while True:
        try:
            n = get_inteiro('Escolha uma linguagem: ')
            nome_linguagem = linguagens[n - 1]
        except:
            print('Não existe essa linguagem!')
        else: 
            break

    linguagens.remove(nome_linguagem)
    return nome_linguagem


def get_framework(frameworks):
    i = 1
    for framework in frameworks:
        print(f'{i} - {framework}')
        i += 1
    
    while True:
        try:
            n = get_inteiro('Escolha um framework: ')
            nome_framework = frameworks[n - 1]
        except:
            print('Não existe esse framework!')
        else:
            break
    
    frameworks.remove(nome_framework)
    return nome_framework


def get_banco_dados(bancos_dados):
    i = 1
    for banco in bancos_dados:
        print(f'{i} - {banco}')
        i += 1
    
    while True:
        try:
            n = get_inteiro('Escola um banco de dados: ')
            nome_banco = bancos_dados[n - 1]
        except:
            print('Não existe esse banco de dados!')
        else:
            break

    bancos_dados.remove(nome_banco)
    return nome_banco


def verifica_dados(lista):
    for linha in lista:

        if linha['linguagem'] == 'Java' and linha['banco_dados'] != 'PostgreSQL':
            return False        

        if linha['framework'] == 'Vue' and linha['programador'] == 'Nicole':
            return False
        
        if linha['framework'] == 'Angular' and linha['banco_dados'] != 'MongoDb':
            return False

        if linha['programador'] == 'Mateus' and linha['linguagem'] != 'Python':
            return False
        
        if linha['programador'] == 'Mateus' and linha['banco_dados'] == 'MySqlServer':
            return False

        if linha['programador'] == 'Tiago' and linha['linguagem'] == 'PHP':
            return False

    return True