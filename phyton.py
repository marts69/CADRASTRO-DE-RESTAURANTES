import os #importa a biblioteca os 

restaurantes = [{"nome":"Praça", "categoria":"Japonesa", "ativo":False},
                {"nome":"Pizzaria Alegria", "categoria":"Pizza", "ativo":True},
                {"nome":"Churrascaria", "categoria":"Churrasco", "ativo":False}] #cria uma lista de restaurantes

def exbir_nome_do_arquivo():
    '''Essa função exibe o nome do arquivo'''
    print("Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n")

def exibir_subtitulo(texto):
    '''Essa função exibe um texto entre linhas de asteriscos
    e limpa a tela do terminal'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def exbir_opcoes():
    """Essa função exibe as opções do menu"""
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar o estado do restaurante")
    print("4. Sair\n")

def Finalizar_App():
    '''Essa função finaliza o app'''

    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    '''Essa função exibe uma mensagem e aguarda o usuário digitar uma tecla para voltar ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def listar_restaurantes():
    '''Essa função lista os restaurantes cadastrados
    Inputs: 
    - listar os restaurantes
    Outputs:
    - Exibe os restaurantes cadastrados'''
    exibir_subtitulo('Listando restaurantes')
    print('Nome'.ljust(20), 'Categoria'.ljust(20), 'Ativo')
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = restaurante["ativo"]
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Esssa função cadastra um novo restaurante
    Inputs : 
    - Nome do restaurante
    - Categoria
    Outputs:
    - Adiciona o restaurante na lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante: {nome_do_restaurante}')
    dados_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def alterar_status_restaurante():
    '''Essa função altera o estado de um restaurante
    Inputs:
    - Nome do restaurante
    - Altera o estado do restaurante
    outputs:
    - Exibe o estado do restaurante
    - Retorna uma mensagem de erro caso o restaurante não seja encontrado'''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            print(f'O estado do restaurante {nome_restaurante} foi alterado para {restaurante["ativo"]}')

    if not restaurante_encontrado:
        print(f'Restaurante {nome_restaurante} não encontrado.')

    voltar_ao_menu_principal()

def opcao_invalida(opcao=None):
    if opcao == 2:
        listar_restaurantes()
    else:
        print("Opção inválida. Tente novamente.")

def escolher_opcao():
    '''Essa função recebe a opção escolhida pelo usuário e chama a função correspondente'''
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
        elif opcao_escolhida == 4:
            Finalizar_App()
        else:
            opcao_invalida(opcao_escolhida)
            return
        voltar_ao_menu_principal()
    except ValueError:
        opcao_invalida()

def main():
    '''Essa função é a principal do programa
    inputs:
    - Exibe o nome do programa
    - Exibe as opções do menu
    - Recebe a opção escolhida pelo usuário
    Outputs:
    - Chama a função correspondente a opção escolhida
    - Retorna uma mensagem de erro caso a opção escolhida seja inválida
    - Retorna uma mensagem de erro caso o valor inserido não seja um número'''
    os.system('cls')
    exbir_nome_do_arquivo()
    exbir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()