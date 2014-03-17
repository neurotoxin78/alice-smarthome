#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from os import path
from subprocess import call
import logging
urllib3_logger = logging.getLogger('urllib3')
urllib3_logger.setLevel(logging.CRITICAL)


root_path = path.dirname(path.realpath(__file__))[:-16]


class gspeech(object):

    """Docstring for gspeech. """

    def __init__(self):
        """@todo: to be defined1. """
        self.url = 'http://www.google.com/speech-api/v1/recognize?lang=ru-RU&client=chromium'
        self.headers = {'Content-Type':'audio/x-flac; rate=16000' }

    
    def recognize(self):
        """@todo: Docstring for recognize.
        :returns: @todo

        """
        self.files = {'file': open(root_path+'tmp/speech.flac', 'rb')}
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
        
