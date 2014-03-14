#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from os import path
from subprocess import call


class gspeech_api(object):

    """Docstring for recognize. """

    def __init__(self):
        """@todo: to be defined1. """
        self.path=path.dirname(path.realpath(__file__))[:-6]
        self.url = 'http://www.google.com/speech-api/v1/recognize?lang=ru-RU&client=chromium'
        self.headers = {'Content-Type':'audio/x-flac; rate=16000' }

    def record(self, duration):
        """@todo: Docstring for record.

        :duration: @todo
        :returns: @todo
        """
        # Record
        #print u"Начанаю запись"
        cmd ='arecord -d 3 -q -f cd -r 16000 speech.wav '
        call(cmd, shell=True)

        # Convert wav to flac
        cmd = 'sox speech.wav speech.flac gain -n -5 silence 1 5 2%'
        call(cmd, shell=True)
        #print u"* Запись закончена"
        return 0

    def recognize(self):
        """@todo: Docstring for recognize.

        :returns: recognized text or error status

        """
        self.files = {'file': open('speech.flac', 'rb')}
        try:
            r = requests.post(self.url, files=self.files, headers=self.headers)
            try:
                resp = r.json()
            except:
                resp={}
                resp['status'] = 5
            if resp['status'] == 0:
                for items in resp['hypotheses']:
                    if items['confidence'] > 0.4:
                        return items['utterance']
                    else:
                        return 1
            else: return 1
        except requests.exceptions.ConnectionError as e:
            return 1

    def cprocess(self, cmd):
        """@todo: Docstring for cprocess.

        :arg1: @todo
        :returns: @todo

        """
        print cmd

    def listen(self):
        """@todo: Docstring for listen.
        :returns: @todo

        """
        magic_word = u'алиса'

        while True:
            self.record(3)
            text = self.recognize()
            if text != 1:
                if text == magic_word:
                    print "Слушаю!"
                    self.record(3)
                    self.cprocess(self.recognize())
        
