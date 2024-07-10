def factorial(number:int):
    value:int = 1
    for i in range(number):
       value = value * (i + 1)

    return value


def calculate_sequence(numerator:float, increment:float, limit:int):
    sequence = []

    for i in range(2, limit + 1):
        term = numerator / factorial(i)
        sequence.append(term)
        numerator += increment

    return sequence


def calculate_final_sum(numerator:float, increment:float, limit:int):
    sum = 0

    for i in range(2, limit + 1):
        term = numerator / factorial(i)
        sum += term
        numerator += increment

    return sum


def main():
    limit:int = 10
    numerator:float = 224
    increment:float = 4
    sum:float = calculate_final_sum(numerator=numerator, increment=increment, limit=limit)
    sequence:list = calculate_sequence(numerator=numerator, increment=increment, limit=limit)

    print("Sequência Calculada:", sequence)
    print("Somatório Final:", sum)


if __name__== "__main__":
    main()
