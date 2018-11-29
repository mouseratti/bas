import subprocess

if __name__ == '__main__':

    ### Обычный запуск
    result = subprocess.run('ping ya.ru -c 2'.split())
    ######## Запуск через shell
    result = subprocess.run('ping ya.ru -c 2', shell=True)

    ############ Перенаправление вывода в файл
    result = subprocess.run(
        'ping ya.ru -c 2'.split(),
        stdout=open("stdout.log.log", "a"),
    )
    #### сбор вывода
    result = subprocess.run('ping ya.ru -c 3',stdout=subprocess.PIPE)

    ##### Остановка по тайм ауту
    try:
        result = subprocess.run('ping ya.ru'.split(),timeout=2)
    except subprocess.TimeoutExpired:
        print("timeout expired!!")


    ###### неблокирующий запуск
    result = subprocess.Popen("ping ya.ru -c 4".split(), stdout=subprocess.PIPE)
    while True:
        if result.poll() is not None:
            break
        else:
            print("process is running!!!")


