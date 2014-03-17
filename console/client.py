#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import cmd
import SOAPpy

server = SOAPpy.SOAPProxy("http://127.0.0.1:3333/")
#resp = server.say('test')
#print resp

class Terminal(cmd.Cmd):

    """Docstring for Terminal. """

    def __init__(self):
        """@todo: to be defined1. """
        cmd.Cmd.__init__(self)

    def do_talk(self,  e):
        """@todo: Docstring for do_say.

        :e: @todo
        :text: @todo
        :returns: @todo

        """
        d = ''
        while d != "bye":
            d = raw_input("<< ")
            if d == 'bye':
                break
            else:
                print ">> " + server.say(d.decode('utf-8'))
    
    def do_exit(self, e):
        """@todo: Docstring for do_exit.

        :e: @todo
        :returns: @todo

        """
        return True

if __name__ == "__main__":
    term = Terminal()
    term.cmdloop()
        
