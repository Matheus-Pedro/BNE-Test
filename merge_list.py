SIZE_LIST:int = 50

def merge_list(first_list:list, second_list:list):
    merged_list = []

    for i in range(SIZE_LIST):
        merged_list.append(first_list[i])
        merged_list.append(second_list[i])

    return merged_list


def find_average_values_from_list(numbers_list:list):
    sum:int = 0

    for i in range(len(numbers_list)):
        sum = sum + numbers_list[i]

    average = sum / len(numbers_list)
    return average


def prompt_list(size):
    numbers_list = []

    print(f"Informe {size} números para preencher a lista:")

    for i in range(size):
        number = int(input(f"Item {i+1}:"))
        numbers_list.append(number)

    return numbers_list


def main():
    first_numbers_list = prompt_list(size = SIZE_LIST)
    second_numbers_list = prompt_list(size = SIZE_LIST)

    merged_list = merge_list(first_list=first_numbers_list, second_list=second_numbers_list)

    print(f"Lista intercalada: {merged_list}")
    print(f"Média dos valores intercalados: {find_average_values_from_list(merged_list)}")


if __name__ == "__main__":
    main()
