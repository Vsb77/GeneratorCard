import random
import os
while True:
    #os.system('cls' if os.name == 'nt' else 'clear')
    def generate(bin):
        pan = random.randint(100000000, 999999999)
        pan = str(bin) + str(pan)
        pan_l = list(map(int, pan))
        pan_l = [num * 2 if index % 2 == 0 else num for index, num in enumerate(pan_l)]
        for i in range(len(pan_l)):
            if pan_l[i] >= 10:
                pan_l[i] = pan_l[i] - 9
        b = sum(pan_l) % 10
        if b == 0:
            c = 0
        else:
            c = 10 - b
        return(str(pan) + str(c))
    print("Введите первые цифры номера или оставьте пустым для автоматической генерации")
    print("Visa - 4\nAmerican Express - 3\nMasterCard - 5\nMaestro - 3,5,6\nJCB International - 3\nChina UnionPay - 6")
    bin = str(input("Выберите цифру или нажмите Enter: "))
    b = bin + str(random.randint(100000, 999999))
    b = [int(i) for i in str(b)]
    b = b[:6]
    bin = str(''.join(map(str, b)))
    formatted_number = ' '.join(map(''.join,zip(*[iter(str(generate(bin)))]*4)))
    print(f"Number card: {formatted_number}")
    c = input("Нажмите ENTER для повтора")