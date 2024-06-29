def sequence(n):
    sequence = []
    number = 1

    while len(sequence) < n:
        sequence.extend([number] * number)
        number += 1

    print(sequence[:n])


if __name__ == "__main__":
    n = int(input("Введите количество элементов n в последовательности: "))
    sequence(n)
