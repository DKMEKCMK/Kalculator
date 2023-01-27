kolChis = int(input("Введите кол-во чисел: "))
znak = input("Введите знак: ")
promezh = 0
if(znak == '**' and kolChis != 2):
    print("Ошибка! Нельзя возвести в степень больше 2х чисел.")
else:
    match znak:
        case '+':
            for schetch in range(kolChis):
                promezh += int(input("Введите число: "))
            print("Сумма чисел: ", promezh)
        case '-':
            promezh = int(input("Введите число: "))
            for schetch in range(kolChis - 1):
                promezh -= int(input("Введите число: "))
            print("Разность чисел: ", promezh)
        case '*':
            promezh = 1
            for schetch in range(kolChis):
                promezh *= int(input("Введите число: "))
            print("Произведение чисел: ", promezh)
        case '/':
            promezh = int(input("Введите число: "))
            for schetch in range(kolChis - 1):
                x = int(input("Введите число: "))
                if(x == 0):
                    print("Делить на 0 нельзя!")
                    while(x == 0):
                        x = int(input("Введите число отличное от 0: "))
                promezh /= x
            print("Частное чисел: ", promezh)
        case '**':
            number1 = int(input("Введите число: "))
            number2 = int(input("Введите степень: "))
            print("Ответ: ", number1 ** number2)
 
