# coding: utf-8

from time import strftime, localtime
from os import system, listdir
from sys import argv
import glob

def log():
    nowTime = strftime("%Y-%m-%d-%H-%M-%S", localtime())
    fileName = 'log-'+str(nowTime)+'.txt'
    cmd = 'git log --decorate --oneline --all --graph >> '+fileName
    if system(cmd) == 0:
        print("Finished!")
    else:
        print("Error! Unknown Error!")
    fileList = listdir()
    logList = [i for i in fileList if 'log' in i]
    logList.sort(reverse=True)
    if len(logList) < 2:
        pass
    else:
        newFile = open(logList[0], 'r+')
        oldFile = open(logList[1], 'r+')
        if newFile.read() == oldFile.read():
            system('rm -rf '+logList[0])
        else:
            pass
    exit(0)

def upload(choice=0, branchName='master', lists=[]):
    del lists[0]
    if choice == 0:
        commitNote = str(input("Enter what note you want to announce :\t"))
    else:
        commitNote = ' '.join(lists)
    openIgnoreFile = open('.gitignore', 'r+')
    allIgnoreFile = openIgnoreFile.readlines()
    openIgnoreFile.close()
    shouldIgnoreFiles = []
    for i in allIgnoreFile:
        if '# ' in i:
            continue
        else:
            shouldIgnoreFiles.append(i.replace('\n', ''))
    foundIgnoreFiles = []
    for i in shouldIgnoreFiles:
        tmp = glob.glob(i)
        for j in tmp:
            if len(str(j)) < 1:
                continue
            else:
                foundIgnoreFiles.append(str(j))
    for i in listdir():
        if i in foundIgnoreFiles:
            continue
        elif '.git' in i:
            continue
        else:
            system(r'git add "'+str(i)+r'"')
            print(str(i)+'\twill be added!')
    system(r'git commit -m "%s"' %commitNote )
    system('git push -u origin '+branchName)

if __name__ == '__main__':
    lists = argv
    if lists[1] == 'upload':
        del lists[0]
        del lists[0]
        upload(1, lists[0], lists)
    elif lists[1] == 'log':
        log()
    else:
        print("Unknown Command!")
    exit(0)

