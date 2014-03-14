#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.recognize import gspeech_api as gspeech
g=gspeech()
#g.record(3)
#print g.recognize()
g.listen()
