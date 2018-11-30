import subprocess
import sys
# sys.stdout

if __name__ == '__main__':

    ### Обычный запуск ['ping', 'ya.ru', '-c', '2']
    result = subprocess.run('ping ya.ru -c 2'.split())

    ######## Запуск через shell
    result = subprocess.run('ping ya.ru -c 2', shell=True)

    ############ Перенаправление вывода в файл
    result = subprocess.run(
        'ping ya.ru -c 2'.split(),
        stdout=open("stdout.log", "a"),
    )
    #### сбор вывода
    result = subprocess.run('ping ya.ru -c 3', stdout=subprocess.PIPE)
    output = result.stdout.decode()

    ##### Остановка по тайм ауту
    try:
        result = subprocess.run('ping ya.ru'.split(),timeout=2)
    except subprocess.TimeoutExpired:
        print("timeout expired!!")
        result.kill()


    ###### неблокирующий запуск
    result = subprocess.Popen(
        "ping ya.ru -c 24".split(),
        stdout=subprocess.PIPE)
    while True:
        if result.poll() is not None:
            break
        else:
            print("process is running!!!")


