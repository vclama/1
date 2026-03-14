import datetime

def main():
    # Получаем текущее время
    now = datetime.datetime.now()
    print(f"Привет! Сейчас {now.strftime('%H:%M')}.")
    print("Бот готов к работе. Это тестовый запуск.")

if __name__ == "__main__":
    main()