from typing import List, Dict
from time import sleep
from models.produto import Produto
from utils.helper import formata_float_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('=' * 50)
    print(' Bem vindo(a)! '.center(50, '#'))
    print(' MercadoPy '.center(50, '#'))
    print('=' * 50)
    print(
        '\n'
        'Selecione uma opção:\n'
        '1- Cadastrar produto\n'
        '2- Listar produto\n'
        '3- Comprar produto\n'
        '4- Visualizar carinho\n'
        '5- Fechar pedido\n'
        '6- Sair'
    )
    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida.')
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print('=' * 50)
    print(' Cadastrar Produto '.center(50, '#'))
    print('=' * 50)

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print('=' * 50)
    print(f' {produto.nome} cadastrado! '.center(50, '#'))
    print('=' * 50)

    sleep(1.5)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('=' * 50)
        print(' Listagem de Produtos '.center(50, '#'))
        print('=' * 50)
        for produto in produtos:
            print(produto)
            print('-' * 50)
            sleep(0.8)
    else:
        print('Ainda não existem produtos cadastrados.')

    sleep(1.5)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('=' * 50)
        print(' Produtos Disponíveis '.center(50, '#'))
        print('=' * 50)
        for produto in produtos:
            print(produto)
            print('-' * 50)
            sleep(0.8)
        codigo: int = int(input('Informe o código do produto que deseja adicionar: '))

        produto: Produto = pega_produto_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                in_carrinho: bool = False
                for item in carrinho:
                    qtd: int = item.get(produto)
                    if qtd:
                        item[produto] = qtd + 1
                        print(f'{produto.nome} agora tem {item[produto]} unidades no carrinho.')
                        in_carrinho = True
                        sleep(1.5)
                        menu()
                if not in_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'{produto.nome} adicionado ao carrinho!')
                    sleep(1.5)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'{produto.nome} adicionado ao carrinho!')
                sleep(1.5)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado')
            sleep(1.5)
            menu()

    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(1.5)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        total_carrinho = 0
        for item in carrinho:
            for dados in item.items():
                total_item = dados[1] * dados[0].preco
                print('-' * 50)
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print(f'Total Item: {formata_float_moeda(total_item)}')
                print('-' * 50)
                total_carrinho += total_item
                sleep(0.8)
        print('-' * 50)
        print(f'Total do carrinho: {formata_float_moeda(total_carrinho)}')
        print('-' * 50)
    else:
        print('Carrinho vazio.')
    sleep(1.5)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        print('=' * 50)
        print(' Carrinho '.center(50, '#'))
        print('=' * 50)
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('=' * 50)
                sleep(1)
        print(f'O valor total é: {formata_float_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(1.5)
    menu()


def pega_produto_codigo(codigo: int) -> Produto:
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
