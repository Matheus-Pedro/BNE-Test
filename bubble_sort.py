def bubble_sort(list:list) :
    for i in range(len(list)) :
        for j in range(i, len(list)) :
            if list[i] > list[j] :
                list[i], list[j] = list[j], list[i]
            
    return list


def reverse_bubble_sort(list:list) :
    for i in range(len(list)) :
        for j in range(i, len(list)) :
            if list[i] < list[j] :
                list[i], list[j] = list[j], list[i]
            
    return list


def prompt_for_name():
    return input("Digite seu nome:")


def prompt_for_item(index:int):
    while True:
        try:
            item:int = int(input(f"Informe o item {index + 1}:"))
            return item
        except:
            print("\n\nERRO NA ENTRADA.\nDigite apenas números inteiros.\n\n")


def prompt_for_items(size:int):
    items_list:list = []
    
    for i in range(size):
        item:int = prompt_for_item(index=i)
        items_list.append(item)
    
    return items_list


def main():
    size:int = len(prompt_for_name())
    items_list:list = prompt_for_items(size=size)
    print(bubble_sort(items_list))
    print(reverse_bubble_sort(items_list))


if __name__ == "__main__":
    main()
