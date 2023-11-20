import time


set_letters = ["омхр", "рткаук", "арсед", "таубн"]

choice_right_words = [
    ["мох", "хром", "ром", "ом"], ["куртка", "утка", "акр"],
    ["адрес", "сад", "среда"], ["табун", "бунт", "тан"]
]


def get_game():
    i = 0
    start_time = time.time()
    level = set_letters[i]

    combination_wins_index = choice_right_words[i]
    print(f"Даны буквы {level}")
    right_word = len(combination_wins_index)
    user = input(f"Необходимо из букв {level.upper()} составить слово. Осталось {right_word} слов ").lower()
    while True:

        if user in combination_wins_index:
            combination_wins_index.remove(user)
            print(f"Слово {user.upper()} есть в загаданных.")
            right_word -= 1
            if right_word != 0:
                user = input(f"Необходимо из букв {level.upper()} составить слово. Осталось {right_word} слов ").lower()
            else:
                end_time = time.time()
                print(f"Level-{i + 1} пройден за {round(end_time - start_time, 2)} секунд. Поздравляем! ")

                player = input(
                    "Выберите продолжить игру командой 'далее' или завершите игру командой 'выход'! ").lower()
                commands = ["далее", "выход"]
                if player in commands[0]:

                    get_game()
                    i += 1
                    break
                elif player in commands[1]:
                    print("Игра завершена! ")
                    break
                else:
                    print("Не правильно ввели данные!")
                    input("Выберите продолжить игру командой 'далее' или завершите игру командой 'выход'! ").lower()
        else:
            print(f"Слова {user.upper()} нет в загаданных")
            user = input(f"Необходимо из букв {level.upper()} составить слово. Осталось {right_word} слов ").lower()


if __name__ == "__main__":
    get_game()
