def how_many_times_letter_appear_in_message(letter: str, message: str) -> int:
    splited_message = [x for x in message.lower()]
    return splited_message.count(letter)


def letter_exists_in_message(letter: str, message: str) -> bool:
    times_letter_appears = how_many_times_letter_appear_in_message(letter, message)

    return times_letter_appears == 0, times_letter_appears


if __name__ == "__main__":
    letter = "e"
    message = "testeeee"

    does_letter_appear, appears_times = letter_exists_in_message(letter, message)

    if does_letter_appear:
        print(f"A letra {letter} não aparece nenhuma vez :(")

    print(
        f'A letra que você me informou ("{letter}") foi encontrada {appears_times} vezes!'
    )
