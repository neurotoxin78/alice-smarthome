#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from os import path
from subprocess import call
import urllib2, urllib


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
        cmd ='arecord -d 3 -q -f cd -r 16000 tmp/speech.wav '
        call(cmd, shell=True)

        # Convert wav to flac
        cmd = 'sox tmp/speech.wav tmp/speech.flac gain -n -5 silence 1 5 2%'
        call(cmd, shell=True)
        #print u"* Запись закончена"
        return 0

    def recognize(self):
        """@todo: Docstring for recognize.

        :returns: recognized text or error status

        """
        self.files = {'file': open('tmp/speech.flac', 'rb')}
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
        if cmd == u'как дела':
            self.speek(u"Отлично, а у вас")

    def speek(self,  text):
        """@todo: Docstring for speek.

        :text: @todo
        :returns: @todo

        """
        url = 'http://translate.google.com/translate_tts?tl=ru&q='+ urllib.quote_plus(text.encode('utf-8'))       
        request = urllib2.Request(url)
        request.add_header('User-agent', 'Mozilla/5.0') 
        opener = urllib2.build_opener()

        f = open("tmp/request.mp3", "wb")
        f.write(opener.open(request).read())
        f.close()
        cmd = 'mpg321 -q -w sounds/request.wav tmp/request.mp3'
        call(cmd, shell=True)
        self.playsound('request')
        

    def playsound(self, sound):
        """@todo: Docstring for play.

        :sound: @todo
        :returns: @todo

        """
        call('aplay -q sounds/'+sound+'.wav', shell=True)
        

    def listen(self):
        """@todo: Docstring for listen.
        :returns: @todo

        """
        magic_word = u'алиса'

        while True:
            self.record(3)
            text = self.recognize()
            print text
            if text != 1:
                if text == magic_word:
                    print "Слушаю!"
                    self.playsound('ready')
                    self.record(3)
                    self.cprocess(self.recognize())
        
