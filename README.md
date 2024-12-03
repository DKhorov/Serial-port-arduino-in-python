# Serial Port Arduino in Python ( Beta Version Cascade Manager )
DK Studio Production 
## Описание проекта

Этот проект предназначен для подключения к устройству Arduino через последовательный порт (COM-порт) и получения данных с него. Программа ждет ввода команды "привет" в консоли для начала процесса подключения. После подключения программа непрерывно получает данные от Arduino и выводит их в консоль.

## Требования

Для работы программы необходимо установить следующие компоненты:
- Python 3.x
- Библиотека `pyserial`

### Установка

1. Установите библиотеку `pyserial` с помощью pip:

    ```sh
    pip install pyserial
    ```

### Использование

1. **Подключите устройство Arduino к компьютеру.**
2. **Убедитесь, что Arduino подключено к указанному COM-порту (например, COM10).**

### Запуск программы

1. Склонируйте этот репозиторий на ваш локальный компьютер:

    ```sh
    git clone https://github.com/DKhorov/Serial-port-arduino-in-python.git
    ```

2. Перейдите в каталог репозитория:

    ```sh
    cd Serial-port-arduino-in-python
    ```

3. Запустите программу:

    ```sh
    python arduino_connection.py
    ```

4. Когда появится приглашение, введите "привет" в консоли для начала подключения:

    ```sh
    > привет
    ```

### Как это работает

Программа выполняет следующие шаги:

1. **Ожидание ввода пользователя:** Программа ждет, пока пользователь введет слово "привет" в консоли для начала процесса подключения.
2. **Подключение к Arduino:** После ввода команды программа пытается подключиться к устройству Arduino на указанном COM-порту (по умолчанию COM10) с использованием скорости передачи данных 9600 бод.
3. **Получение данных:** После успешного подключения программа непрерывно получает данные от Arduino и выводит их в консоль. Программа завершает работу при нажатии Ctrl+C.
   
### Автор пректа
© Copyright DK Studio All rights reserved 2023-2024 
### Пример кода

```python
import serial
import time

def connect_arduino(port, baudrate=9600):
    try:
        arduino = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # Ожидание подключения
        print(f"Подключение к Arduino на порту {port} установлено")
        return arduino
    except serial.SerialException:
        print(f"Не удалось подключиться к Arduino на порту {port}")
        return None

def main():
    print("Введите 'привет' для подключения к Arduino:")
    while True:
        user_input = input("> ").strip().lower()
        if user_input == "привет":
            arduino_port = 'COM10'  # Порт, к которому подключен Arduino
            arduino = connect_arduino(arduino_port)

            if arduino:
                print("Начинаем получение данных с Arduino. Для выхода нажмите Ctrl+C.")
                try:
                    while True:
                        if arduino.in_waiting > 0:
                            line = arduino.readline().decode('utf-8').rstrip()
                            print(f"Получено от Arduino: {line}")
                except KeyboardInterrupt:
                    print("Завершение работы.")
                    arduino.close()  # Закрытие соединения по завершении работы
            break
        else:
            print("Неправильный ввод. Попробуйте еще раз.")

if __name__ == "__main__":
    main()



