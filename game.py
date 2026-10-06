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
def play_game(state):
    print("\n--- Игра началась! Удачи! ---")
    while True:
        if len(state["fixed_errors"]) == 3:
            print("\nПОБЕДА! Все ошибки исправлены, стенд готов к демо!")
            break
        if state["turns"] == 0:
            print("\nПОРАЖЕНИЕ! Ходы закончились, вы не успели до демо.")
            break
        if state["energy"] < 2:
            if state["charger"] == True and "Зарядка" not in state["inventory"]:
                print("\nПОРАЖЕНИЕ! Энергии меньше 2, а возможностей зарядиться больше нет.")
                break
        print(f"\n[Осталось ходов: {state['turns']} | Энергия: {state['energy']}]")
        b = input("Выберите действие: ").strip()
        if b == "0":
            print("Текущая игра завершена. Возвращаемся в меню.")
            break
        elif b == "1":
            pass
        elif b == "2":
            pass
        elif b == "3":
            pass
        elif b == "4":
            pass
        elif b == "5":
            pass
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
        a = (input("Выберите: "))
        if a == "0":
            break
        elif a == "1":
            state = start_status()
            play_game(state)
        elif a == "2":
            rule()
        else:
            print("Неизвестная команда! Ход не засчитан. Попробуйте снова.")
menu()