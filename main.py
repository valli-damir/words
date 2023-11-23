import time

set_letters_array = ["омхр", "рткаук", "арсед", "таубн"]

choice_right_words_array = [
    ["мох", "хром", "ром", "ом"], ["куртка", "утка", "акр"],
    ["адрес", "сад", "среда"], ["табун", "бунт", "тан"]
]


def get_game():
    full_game_time = 0.0

    for i in range(0, len(set_letters_array)):
        level_start_time = time.time()

        level = set_letters_array[i]
        print(f"Даны буквы {level}")

        combinations = choice_right_words_array[i]
        right_word = len(combinations)

        while right_word != 0:
            user_input = input(
                f"Необходимо из букв {level.upper()} составить слово. Осталось {right_word} слов ").lower()

            if user_input in combinations:
                combinations.remove(user_input)
                print(f"Слово {user_input.upper()} есть в загаданных.")
                right_word -= 1

                if right_word == 0:
                    end_time = time.time()
                    level_time = end_time - level_start_time
                    print(f"Level-{i + 1} пройден за {round(level_time, 2)} секунд. Поздравляем! ")

                    full_game_time += level_time

                    player_input = input(
                        "Выберите продолжить игру командой 'далее' или завершите игру командой 'выход'! ").lower()
                    commands = ["далее", "выход"]

                    while player_input != commands[0]:
                        if player_input in commands:
                            if player_input == commands[1]:
                                print("Игра завершена! ")
                                print(f"Игра пройдена за {round(full_game_time, 2)}, секунд")
                                exit()
                        else:
                            print("Не правильно ввели данные!")
                            player_input = input(
                                "Выберите продолжить игру командой 'далее' или "
                                "завершите игру командой 'выход'! ").lower()

            else:
                print(f"Слова {user_input.upper()} нет в загаданных")

    print("Игра завершена! ")
    print(f"Игра пройдена за {round(full_game_time, 2)} секунд")


if __name__ == "__main__":
    get_game()
