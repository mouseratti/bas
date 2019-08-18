"""
Дано число n. С начала суток прошло n минут.
Определите, сколько часов и минут будут показывать электронные часы в этот момент.
Программа должна вывести строку в формате "HH:mm"
"""
GREETING = "Введите количество минут, прошедших с начала суток. "
minutes_in_one_hour = 60
while True:
    minutes = input(GREETING)
    if minutes:
        try:
            minutes = int(minutes)
            break
        except:
            print("Введено некорректное значение!!!")

hours_count = minutes // minutes_in_one_hour
minutes_count = minutes % minutes_in_one_hour
print("{:02}:{:02}".format(hours_count, minutes_count))
