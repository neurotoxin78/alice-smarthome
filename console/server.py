#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
root_path = path.dirname(path.realpath(__file__))[:-7]
from SOAPpy import *
import logging as Log
Log.basicConfig( level = Log.DEBUG,format = '%(name)s -  %(message)s' )
from neocortex.processing.processing import process
from common.sql import sql



class Server(object):

    """Docstring for Server. """

    def __init__(self):
        """@todo: to be defined1. """
        self.p = process()

    
    def say(self,  text):
        """@todo: Docstring for say.

        :text: @todo
        :returns: @todo

        """
        a = self.p.find_action_for(text)
        try:
            answer = a[0][0]
        except:
            answer = u"не понятно"
        return answer



class cons(object):

    """Docstring for cons. """

    def __init__(self):
        """@todo: to be defined1. """
        self.log = Log.getLogger('Alice-Console:')

        
    def start(self):
        self.log.info(u'Запуск сервера консоли')
        server = SOAPServer(('0.0.0.0', 3333))
        obj = Server()
        server.registerObject(obj)
        server.serve_forever()

if __name__ == "__main__":
    c = cons()
    c.start()

