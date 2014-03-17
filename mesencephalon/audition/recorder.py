#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
from subprocess import call

root_path = path.dirname(path.realpath(__file__))[:-22]
#print root_path

class recorder(object):

    """Docstring for recorder. """

    def __init__(self):
        """@todo: to be defined1. """
        self.recpath = root_path + 'tmp/'
    def record(self, duration):
        """@todo: Docstring for recodrd.

        :duration: @todo
        :returns: @todo

        """
        # Record
        #print u"Начанаю запись"
        cmd ='arecord -d 3 -q -f cd -r 16000 '+self.recpath+'speech.wav '
        call(cmd, shell=True)

        # Convert wav to flac
        cmd = 'sox '+self.recpath+'speech.wav '+self.recpath+'/speech.flac gain -n -5 silence 1 5 2%'
        call(cmd, shell=True)
        #print u"* Запись закончена"
        return 0
        

