def fibonacci(limit: int) -> list[int]:
    sequence = [0, 1]

    while limit > sequence[-1]:
        next_fib_value = sequence[-1] + sequence[-2]
        sequence.append(next_fib_value)

    return sequence


def belongs_to_fibonacci(number: int):
    fib_sequence = fibonacci(number)

    return fib_sequence.count(number) == 1


if __name__ == "__main__":
    number_to_check = 14
    print(f"O número {number_to_check}", end=" ")

    if belongs_to_fibonacci(number_to_check):
        print("pertence à sequencia de fibonacci")

    else:
        print("não pertence à sequencia de fibonacci")
