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
    print("Cascade Manager - Sync and Dev toolsg")
    time.sleep(1) 
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
