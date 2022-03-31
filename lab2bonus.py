import subprocess


def ping(data):
    label = ''.join(data)
    result = subprocess.getoutput(f"Адреса мережі {label}")
    print(result)


def echo(data):
    print(" ".join(data))


def login(data):
    if len(data) != 2:
        print("Неправильно введений  login або password")
    else:
        print("Успішно виконав вхід.")


def list(data):
    label = ''.join(data)
    result = subprocess.getoutput(f"dir {label}")
    print(result)


def msg(data):
    if len(data) != 2:
        print("Неправильно введений destinationUser або text")
    else:
        print(f"Лист надіслано користувачу {data[0]}.")


def file(data):
    if len(data) != 2:
        print(
            "Непраправильно введено destinationUser або filename")
    else:
        print(f"Файл '{data[1]}' надіслано користувачу {data[0]}.")


def splitter(text):
    text = text.split()
    command = text.pop(0)
    data = text
    return command, data


def main():
    command, data = splitter(input("Введіть команду\n"))
    print(f"Команда: {command}; Параметри: {data}")
    if command == 'ping':
        ping(data)
    elif command == 'echo':
        echo(data)
    elif command == 'login':
        login(data)
    elif command == 'list':
        list(data)
    elif command == 'msg':
        msg(data)
    elif command == 'file':
        file(data)
    elif command == 'exit':
        return False
    else:
        print("Не розпізнав команду спробуйте ще раз")
    return True


if __name__ == "__main__":
    while True:
        if main() == False:
            break
