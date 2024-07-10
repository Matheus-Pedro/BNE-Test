SIZE_LIST:int = 2

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

    average:float = sum / len(numbers_list)
    return average


def prompt_for_item(index):
    number:int = int(input(f"Item {index+1}:"))
    return number


def create_list(size:int):
    print(f"Informe {size} números para preencher a lista:")
    while True:
        try:
            numbers_list:list = []
            
            for i in range(size):
                numbers_list.append(prompt_for_item(i))

            return numbers_list
        
        except: 
            print("\nERRO NA ENTRADA.\nDigite apenas números inteiros.\n")


def main():
    first_numbers_list:list = create_list(size = SIZE_LIST)
    second_numbers_list:list = create_list(size = SIZE_LIST)

    merged_list:list = merge_list(first_list=first_numbers_list, second_list=second_numbers_list)

    print(f"Lista intercalada: {merged_list}")
    print(f"Média dos valores intercalados: {find_average_values_from_list(merged_list)}")


if __name__ == "__main__":
    main()
