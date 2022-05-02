from ex115.interface import *


def arquivo_existe(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ler_arquivo(nome):
    try:
        arq = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for line in arq:
            dado = line.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:34}{dado[1]:>3} anos')
        arq.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        arq = open(arquivo, 'at')
    except:
        print('Hou um ERRO na abertura do arquivo!')
    else:
        try:
            arq.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            arq.close()
