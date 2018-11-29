import subprocess

def subproc():
    result = subprocess.run(
    'ping ya.kz -c 2'.split(),
    stdout=("stdout.log", "a")
return result


# def stat():
#     f = open("stdout.log", "r")
#     pscount = (
