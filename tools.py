#coding:utf-8

class ParameterError(Exception):
    def __init__(self, argsName, argsInfo):
        self.argsName = argsName
        self.argsInfo = argsInfo
        self.print = r'ERROR! The Parameter named "%s" has recieved an error info "%s"' %(self.argsName, self.argsInfo)
        self.error = r'Parameter Error!'
    def __str__(self):
        print(self.print)
        return self.error

import time, sys

__all__ = ['printf', '__all__']

def printf(info, end='\n', mode='common', delayTime=0):
    if mode == 'common':
        print(str(info), end=end)
    elif mode == 'delay':
        for i in range(len(str(info))):
            print(list(str(info))[i], end=end)
            sys.stdout.flush()
            time.sleep(delayTime/1000)
        print('', end=end)
    else:
        raise ParameterError('mode', mode)

