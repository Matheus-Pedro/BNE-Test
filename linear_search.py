def display_number_found(number: int, item: int):
    print(f'\nO item {number} está na posição {item + 1} da lista.')


def display_number_not_found(number: int):
    print(f'\nO item {number} não foi encontrado, tente novamente utilizando outro número.')


def pesquisar(vet: list, n: int):
    for i in range(len(vet)):
        if vet[i] == n:
            return handle_search_result(in_list=True, item=i, number=n)
    return handle_search_result(in_list=False, item=None, number=n)


def handle_search_result(in_list: bool, item: int, number: int):
    if in_list:
        return display_number_found(number=number, item=item)
    else:
        return display_number_not_found(number=number)


def prompt_for_number():
    while True:
        try:
            text = "CONSULTA UTILIZANDO PESQUISA LINEAR\nInforme um número para consultá-lo em nosso vetor (array, lista):"
            number:int = int(input(text))

            return number
        except:
            print("\nERRO NA ENTRADA.\nDigite apenas números inteiros.\n")


def main():
    the_list:list = [9, 7, 2, 16, 14, 30]
    number:int = prompt_for_number()
    pesquisar(vet=the_list, n=number)


if __name__ == "__main__":
    main()
