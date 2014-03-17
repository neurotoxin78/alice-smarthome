#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3 as lite
from os import path
root_path = path.dirname(path.realpath(__file__))[:-6]

class sql(object):

    """Docstring for sql. """

    def __init__(self):
        """@todo: to be defined1. """

        
    def connect(self,  database=root_path+'memories/memo.db'):
        """@todo: Docstring for connect.

        :database: @todo
        :returns: @todo

        """
        con = lite.connect(database)
        return con

    def get_action_for(self,  data, database=root_path+'memories/memo.db', table='memo'):
        """@todo: Docstring for get.

        :database: @todo
        :data: @todo
        :returns: @todo

        """
        con = self.connect(database)
	with con:
	    cur = con.cursor()
            print data
	    cur.execute('select action from '+table+' where '+table+' MATCH "'+data+'*";')
	return cur.fetchall()
        
