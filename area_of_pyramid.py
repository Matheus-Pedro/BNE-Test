from math import sqrt

BASE_EDGE = 133.2

def prompt_for_pyramid_height():
    return float(input("Informe a altura da pirâmide (em milímetros): "))


def calculate_area_of_pyramid(pyramid_height):
    h = sqrt((BASE_EDGE / 2) ** 2 + pyramid_height ** 2)
    side_face_area = 0.5 * BASE_EDGE * h
    ah = 4 * side_face_area
    ab = BASE_EDGE ** 2
    area_of_pyramid = ab + ah
    return area_of_pyramid


def main():
    pyramid_height = prompt_for_pyramid_height()
    total_area = calculate_area_of_pyramid(pyramid_height)
    print(f"A área total da pirâmide é: {total_area:.2f} mm²")


if __name__ == "__main__":
    main()
