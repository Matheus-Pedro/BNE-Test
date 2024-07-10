from math import sqrt

BASE_EDGE = 133.2


def replace_comma_for_dot(value:str):
    for i in range(len(value)):
        if value[i] == ",":
            value = value.replace(value[i], ".")
        
    return value


def prompt_for_pyramid_height():
    try:
        pyramid_height = input("Informe a altura da pirâmide (em milímetros): ")
        return float(replace_comma_for_dot(pyramid_height))
        
    except:
        print("\n\nERRO NA ENTRADA.\nTente novamente utilizando somente números do conjunto dos reais.\n\n")
        exit()


def calculate_area_of_pyramid(pyramid_height:float):
    side_face_heigth = sqrt((BASE_EDGE / 2) ** 2 + pyramid_height ** 2)
    side_face_area = 0.5 * BASE_EDGE * side_face_heigth

    area_of_side_faces = 4 * side_face_area
    area_of_base = BASE_EDGE ** 2

    area_of_pyramid:float = area_of_base + area_of_side_faces
    return area_of_pyramid


def main():
    pyramid_height:float = prompt_for_pyramid_height()
    total_area:float = calculate_area_of_pyramid(pyramid_height)
    print(f"A área total da pirâmide é: {total_area:.2f} mm²")


if __name__ == "__main__":
    main()
