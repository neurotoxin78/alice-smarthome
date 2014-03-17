#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
root_path = path.dirname(path.realpath(__file__))[:-20]
import pymorphy2
from common.sql import sql

class process(object):

    """Docstring for process. """

    def __init__(self):
        """@todo: to be defined1. """
        self.morph = pymorphy2.MorphAnalyzer()
        self.sq = sql()
    def normalize(self, string):
        """@todo: Docstring for normalize.

        :string: @todo
        :returns: @todo

        """
        slist = string.split()
        nstring = []
        for item in slist:
            p = self.morph.parse(item)[0]
            nstring.append(p.normal_form)
        return nstring

    def find_action_for(self, string):
        """@todo: Docstring for function.

        :arg1: @todo
        :returns: @todo

        """
        for item in self.normalize(string):
            act = self.sq.get_action_for(item)  
            if act:
                action = act
            else:
                action = 1
        return action


