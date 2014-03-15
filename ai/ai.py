#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymorphy2

class AI(object):

    """Docstring for AI. """

    def __init__(self):
        """@todo: to be defined1. """
    def normalize(self,  text):
        """@todo: Docstring for normalize.

        :text: @todo
        :returns: @todo
    """
        morph = pymorphy2.MorphAnalyzer()
        p = morph.parse(text)[0]
        return p.normal_form

if __name__ == "__main__":
    ai = AI()
    d = ai.normalize(u'Величайшего')
    print d

