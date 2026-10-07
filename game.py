def start_status():
    state = {
        "energy": 6,
        "turns": 6,
        "clue": [],
        "inventory": [],
        "charger": False,
        "fixed_errors": []
    }
    return state


def inspect_stand(state):
    if "EKEB" in state["clue"]:
        print("Вы уже осмотрели стенд и нашли улику EKEB.")
        return

    state["clue"].append("EKEB")
    state["turns"] -= 1
    print("\nВы осмотрели стенд и нашли улику: код EKEB!")
    print("Улика добавлена. Теперь доступна Ошибка A.")

# Алихан Абдираманов
def take_charger(state):
    if state["charger"] or "Зарядка" in state["inventory"]:
        print("Вы уже забрали зарядку.")
        return

    state["inventory"].append("Зарядка")
    state["turns"] -= 1

    print("Вы забрали зарядку.")
    print("Зарядка добавлена в инвентарь.")


def use_charger(state):
    if "Зарядка" not in state["inventory"]:
        print("У вас нет зарядки.")
        return

    state["inventory"].remove("Зарядка")
    state["energy"] = min(6, state["energy"] + 3)
    state["turns"] -= 1
    state["charger"] = True

    print("Вы использовала зарядку.")
    print(f"Энергия восстановлена. Сейчас энергии: {state['energy']}.")

#Жусипбеков Арман 
def fix_error(state):
    print("\n--- ИСПРАВЛЕНИЕ ОШИБОК ---")
    if "A" in state["fixed_errors"]:
        print("A: [Исправлена]")
    elif "EKEB" in state["clue"]:
        print("A: Ввести код EKEB [Доступна]")
    else:
        print("A: [Заблокирована: сначала осмотрите стенд и получите улику]")

    if "B" in state["fixed_errors"]:
        print("B: [Исправлена]")
    else:
        print("B: Сколько минут в 2 часах? [Доступна]")

    if "C" in state["fixed_errors"]:
        print("C: [Исправлена]")
    else:
        print("C: Привести ' Almaty ' к нижнему регистру [Доступна]")

    v = input("\nВыберите ошибку (A, B, C) или 0 для отмены: ").strip().upper()

    if v == "0":
        return

    if v in ["A", "А"]:
        if "A" in state["fixed_errors"]:
            print("Ошибка A уже исправлена!")
        elif "EKEB" in state["clue"]:
            if state["energy"] >= 2:
                state["energy"] -= 2
                state["turns"] -= 1
                print(f"\nСписано 2 энергии и 1 ход (Осталось энергии: {state['energy']}, ходов: {state['turns']}).")

                ans = input("Задание: Ввести код EKEB (или 0 для отмены)\nОтвет: ").strip().lower()
                if ans == "ekeb":
                    state["fixed_errors"].append("A")
                    print("Правильно! Ошибка A исправлена.")
                else:
                    print("Неверно!")
            else:
                print(f"Недостаточно энергии! Нужно минимум 2 (у вас: {state['energy']}).")
        else:
            print("Ошибка A недоступна: сначала осмотрите стенд и получите улику!")

    elif v in ["B", "В"]:
        if "B" in state["fixed_errors"]:
            print("Ошибка B уже исправлена!")
        elif state["energy"] >= 2:
            state["energy"] -= 2
            state["turns"] -= 1
            print(f"\nСписано 2 энергии и 1 ход (Осталось энергии: {state['energy']}, ходов: {state['turns']}).")

            ans = input("Задание: Сколько минут в 2 часах?\nОтвет: ").strip().lower()
            if ans == "120":
                state["fixed_errors"].append("B")
                print("Правильно! Ошибка B исправлена.")
            else:
                print("Неверно!")
        else:
            print(f"Недостаточно энергии! Нужно минимум 2 (у вас: {state['energy']}).")

    elif v in ["C", "С"]:
        if "C" in state["fixed_errors"]:
            print("Ошибка C уже исправлена!")
        elif state["energy"] >= 2:
            state["energy"] -= 2
            state["turns"] -= 1
            print(f"\nСписано 2 энергии и 1 ход (Осталось энергии: {state['energy']}, ходов: {state['turns']}).")

            ans = input("Задание: Привести ' Almaty ' к нижнему регистру без пробелов по краям\nОтвет: ").strip().lower()
            if ans == "almaty":
                state["fixed_errors"].append("C")
                print("Правильно! Ошибка C исправлена.")
            else:
                print("Неверно!")
        else:
            print(f"Недостаточно энергии! Нужно минимум 2 (у вас: {state['energy']}).")

    else:
        print("Неизвестный выбор.")


def show_status(state):
    print("\n===== СТАТУС =====")
    print(f"Энергия: {state['energy']}/6")
    print(f"Осталось ходов: {state['turns']}")

    if state["clue"]:
        print(f"Улики: {', '.join(state['clue'])}")
    else:
        print("Улики: нет")

    if state["inventory"]:
        print(f"Инвентарь: {', '.join(state['inventory'])}")
    else:
        print("Инвентарь: пуст")

    print(f"Исправлено ошибок: {len(state['fixed_errors'])}/3")


def play_game(state):
    print("\n--- Игра началась! Удачи! ---")
    while True:
        if len(state["fixed_errors"]) == 3:
            print("\nПОБЕДА! Все ошибки исправлены, стенд готов к демо!")
            break
        if state["turns"] <= 0:
            print("\nПОРАЖЕНИЕ! Ходы закончились, вы не успели до демо.")
            break
        if state["energy"] < 2:
            if state["charger"] and "Зарядка" not in state["inventory"]:
                print("\nПОРАЖЕНИЕ! Энергии меньше 2, а возможностей зарядиться больше нет.")
                break

        print(f"\n[Осталось ходов: {state['turns']} | Энергия: {state['energy']}]")
        print("\n===== ДЕЙСТВИЯ =====")
        print("1. Осмотреть стенд")
        print("2. Забрать зарядку")
        print("3. Использовать зарядку")
        print("4. Исправить ошибку")
        print("5. Посмотреть статус")
        print("0. Выйти в меню")

        b = input("Выберите действие: ").strip()
        if b == "0":
            print("Текущая игра завершена. Возвращаемся в меню.")
            break
        elif b == "1":
            inspect_stand(state)
        elif b == "2":
            take_charger(state)
        elif b == "3":
            use_charger(state)
        elif b == "4":
            fix_error(state)
        elif b == "5":
            show_status(state)
        else:
            print("Неизвестная команда! Ход не засчитан. Попробуйте снова.")


def rule():
    print("===== ПРАВИЛА ИГРЫ =====")
    print("Вы — команда, которая готовит стенд EKEB к демонстрации.")
    print("У вас есть 6 ходов и максимум 6 энергии.")
    print()
    print("1. Осмотреть стенд — получить код EKEB, -1 ход.")
    print("2. Забрать зарядку — добавить её в инвентарь, -1 ход.")
    print("3. Использовать зарядку — +3 энергии, -1 ход.")
    print("4. Исправить ошибку — нужно 2 энергии, -1 ход.")
    print("5. Статус — посмотреть энергию, ходы и инвентарь.")
    print("0. Выход — завершить игру.")
    print()
    print("Цель: исправить все ошибки до окончания ходов!")


def menu():
    while True:
        print("              МЕНЮ")
        print(" ╔════════ДОБРО ПОЖАЛОВАТЬ════════╗")
        print(" ║1.          Начать              ║")
        print(" ║2.          Правила             ║")
        print(" ║0.          Выход               ║")
        print(" ╚════════════════════════════════╝")
        a = input("Выберите: ").strip()
        if a == "0":
            break
        elif a == "1":
            state = start_status()
            play_game(state)
        elif a == "2":
            rule()
        else:
            print("Неизвестная команда! Попробуйте снова.")


menu()
