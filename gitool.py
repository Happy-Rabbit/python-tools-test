# coding: utf-8

from time import strftime, localtime
from os import system, listdir
from sys import argv

def log():
    nowTime = strftime("%Y-%m-%d-%H-%M-%S", localtime())
    fileName = 'log-'+str(nowTime)+'.txt'
    cmd = 'git log --decorate --oneline --all --graph >> '+fileName
    fileList = listdir()
    logList = [i for i in fileList if 'log' in i]
    sorted(logList)
    if system(cmd) == 0:
        print("Finished!")
    else:
        print("Error! Unknown Error!")

    exit(0)

def upload(choice=0, lists=[]):
    if choice == 0:
        commitNote = str(input("Enter what note you want to announce :\t"))
    else:
        commitNote = ' '.join(lists)
    system('git add *')
    system(r'git commit -m "%s"' %commitNote )
    system('git push -u origin master')

if __name__ == '__main__':
    lists = argv
    if lists[1] == 'upload':
        del lists[0]
        del lists[0]
        upload(1, lists)
    elif lists[1] == 'log':
        log()
    else:
        print("Unknown Command!")
    exit(0)

