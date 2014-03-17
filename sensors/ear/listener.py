#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
root_path = path.dirname(path.realpath(__file__))[:-11]
from mesencephalon.audition.recorder import recorder 
from neocortex.speech.recognition import gspeech
from neocortex.processing.processing import process

import logging as Log
Log.basicConfig( level = Log.DEBUG,format = '%(name)s -  %(message)s' )



class listener(object):

    """Docstring for ear. """

    def __init__(self):
        """@todo: to be defined1. """
        self.magic_words={'cmd_mode':u'алиса', 'listen_mode':u'отбой'}
        self.rec = recorder()
        self.gs = gspeech()
        self.log = Log.getLogger('Alice-Ear:')
        self.log.info('Запуск голосового управления...')
        self.proc = process()

    
    def listen_forever(self):
        """@todo: Docstring for listen_forever.
        :returns: @todo

        """
        while True:
             self.rec.record('5')
             data = self.gs.recognize()
             if data == self.magic_words['cmd_mode']:
                self.log.info(u'Слушаю...')
                while True: 
                    if data == self.magic_words['listen_mode']:
                        self.log.info(u'Возвращаюсь в режим прослушивания ...')
                        break
                    else:
                        self.rec.record('3')
                        data = self.gs.recognize()
                        if data != 1:
                            ### Тут обработка комманды
                            ###self.log.info(u"Вы сказали: "+data)
                            try:
                                action = self.proc.find_action_for(data)[0][0]
                            except:
                                action = u'не поняла...'
                            self.log.info(action)
    
