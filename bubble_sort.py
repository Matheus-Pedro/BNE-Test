def bubble_sort(list:list) :
    for i in range(len(list)) :
        for j in range(i, len(list)) :
            if list[i] > list[j] :
                list[i], list[j] = list[j], list[i]
            
    print(list)
    return list


def reverse_bubble_sort(list:list) :
    for i in range(len(list)) :
        for j in range(i, len(list)) :
            if list[i] < list[j] :
                list[i], list[j] = list[j], list[i]
            
    print(list)
    return list


def prompt_for_name():
    return input("Digite seu nome:")


def prompt_for_items(size:int):
    items_list = []
    
    for i in range(size):
        j = int(input(f"Informe o item {i + 1}:"))
        items_list.append(j)
    
    return items_list


def main():
    size = len(prompt_for_name())
    items_list = prompt_for_items(size=size)
    bubble_sort(items_list)
    reverse_bubble_sort(items_list)


if __name__ == "__main__":
    main()
