# Импортируем модуль random для генерации случайного выбора компьютера
import random
from datetime import datetime  # Для сохранения даты результатов


class ScoreBoard:
    """
    Класс для ведения счета и сохранения результатов игры.

    Атрибуты:
        player_wins (int): Количество побед игрока
        computer_wins (int): Количество побед компьютера
        draws (int): Количество ничьих
    """

    def __init__(self):
        """Инициализирует счетчики побед и ничьих"""
        self.player_wins = 0
        self.computer_wins = 0
        self.draws = 0

    def update_score(self, result):
        """
        Обновляет счет на основе результата раунда.

        Параметры:
            result (str): Результат раунда ('player', 'computer' или 'draw')
        """
        if result == 'player':
            self.player_wins += 1
        elif result == 'computer':
            self.computer_wins += 1
        else:
            self.draws += 1

    def display_score(self):
        """Выводит текущий счет на экран"""
        print(f"\nТекущий счет:")
        print(f"Игрок: {self.player_wins} побед")
        print(f"Компьютер: {self.computer_wins} побед")
        print(f"Ничьи: {self.draws}")
        print("=" * 30)

    def save_to_file(self):
        """
        Сохраняет результаты игры в файл scores.txt.
        Формат: Дата | Побед игрока | Побед компьютера | Ничьих
        """
        with open('scores.txt', 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} | {self.player_wins} | {self.computer_wins} | {self.draws}\n")


def determine_winner(user_choice, computer_choice):
    """
    Определяет победителя раунда и возвращает результат для ScoreBoard.

    Возвращает:
        tuple: (сообщение для вывода, результат для счета)
    """
    if user_choice == computer_choice:
        return ("🤝 Ничья!", 'draw')

    win_conditions = {'к': 'н', 'н': 'б', 'б': 'к'}
    if win_conditions[user_choice] == computer_choice:
        return ("🎉 Вы победили!", 'player')
    else:
        return ("💻 Компьютер победил!", 'computer')


def main_game_loop():
    """Основной игровой цикл с системой подсчета очков"""
    print("🎮 Камень, Ножницы, Бумага!")
    print("👉 Для выхода введите 'выход'\n")

    # Инициализируем счетчик
    scoreboard = ScoreBoard()

    while True:
        user_choice = get_user_choice()

        if user_choice == 'выход':
            print("\n🖐️ До свидания!")
            # Перед выходом сохраняем результаты
            scoreboard.save_to_file()
            break

        computer_choice = get_computer_choice()
        print(f"\n👉 Вы: {user_choice}\n💻 Компьютер: {computer_choice}")

        # Получаем и сообщение, и результат для счета
        message, result = determine_winner(user_choice, computer_choice)
        print(f"\n{message}")

        # Обновляем счет
        scoreboard.update_score(result)
        # Показываем текущий счет
        scoreboard.display_score()


def get_computer_choice():
    """
    Генерирует случайный выбор компьютера
    Возвращает:
        'к' - камень
        'н' - ножницы
        'б' - бумага
    """
    # random.choice выбирает случайный элемент из списка
    return random.choice(['к', 'н', 'б'])


def get_user_choice():
    """
    Получает и проверяет ввод пользователя
    Возвращает:
        'к', 'н', 'б' - при корректном вводе
        'выход' - при команде выхода
    Обрабатывает:
        - Некорректный ввод
        - Команды выхода
    """
    while True:  # Бесконечный цикл, пока не получим корректный ввод
        try:
            # Получаем ввод пользователя, приводим к нижнему регистру и удаляем пробелы
            user_input = input("Выберите: камень (к), ножницы (н), бумага (б) или 'выход': ").lower().strip()

            # Проверяем команды выхода (поддерживаются разные варианты)
            if user_input in ['exit', 'quit', 'выход', 'q']:
                # Запрашиваем подтверждение выхода
                confirm = input("Подтвердите выход (д/н): ").lower()
                if confirm in ['д', 'y', 'yes', 'да']:
                    return 'выход'  # Возвращаем команду выхода
                continue  # Продолжаем цикл, если выход не подтвержден

            # Проверяем корректность игрового ввода
            if user_input not in ['к', 'н', 'б']:
                print("❌ Допустимые значения: к, н, б")
                continue  # Продолжаем цикл при некорректном вводе

            return user_input  # Возвращаем корректный выбор

        except Exception as e:
            # Обрабатываем любые другие ошибки ввода
            print(f"⚠️ Ошибка ввода: {e}. Попробуйте еще раз.")


if __name__ == "__main__":
    main_game_loop()