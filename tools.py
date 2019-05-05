# coding:utf-8

r'''
Happy Rabbit developed this module (so...stupid...and...emmm...)

WARNING!
    THIS IS JUST A MODULE!

This module just can make me (maybe) feel convenient.

The function(s) in this module is(are):
    printf

The class(es) in this module is(are):
    ParameterError

The variable(s) in this module is(are):
    __all__
    __author__
    __email__
    (maybe and __builtin__ and so on...)
'''

# IMPORT AREA!

import time, sys

# CLASS AREA!

class ParameterError(Exception):
    r'''
    This Class is used to raised and show the error reason, just like some parameter was given a wrong info...
    '''
    def __init__(self, argsName, argsInfo):
        self.argsName = argsName
        self.argsInfo = argsInfo
        self.print = r'ERROR! The Parameter named "%s" has recieved an error info "%s"' %(self.argsName, self.argsInfo)
        self.error = r'Parameter Error!'
    def __str__(self):
        print(self.print)
        return self.error

# VARIABLE AREA!

__all__ = ['printf', '__all__', '__author__', '__email__']

__author__ = 'Happy Rabbit'

__email__ = 'happy.rabbit.yy@outlook.com'

# FUNCTION AREA!

def printf(info, end='\n', mode='common', delayTime=0):
    r'''
    This function just used to show some info at the screen, it has two modes, one of the modes is "common", just print!,
    another is "delay", it can show the information with few miliseconds delay...

    Usage:
    
    printf(info, end='\n', mode='common', delayTime=0) # return nothing.

    "info" is the message you want to show at the screen.
    "end" is that when the message is end, what string will be add at the end of the message automatically. default is "\n"
    "mode" just has two choice (just for this version) "common" and "delay", if you give it another choice,
        it will raise the "parameterError"! please be carefull when you use it.
    "delayTime" is an integer variable, if "mode" is "common", then "delayTime" will do nothing, but, if "mode" is "delay",
        then "delayTime" will control the delay time...
    '''
    if mode == 'common':
        print(str(info), end=end)
    elif mode == 'delay':
        for i in range(len(str(info))):
            print(list(str(info))[i], end='')
            sys.stdout.flush()
            time.sleep(delayTime/1000)
        print('', end=end)
    else:
        raise ParameterError('mode', mode)

