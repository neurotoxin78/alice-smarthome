#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue

from sensors.ear.listener import listener
from console.server import cons

ears = listener()
csrv = cons()

if __name__ == "__main__":
    plistener=Process(target=csrv.start,args=())
    pcsrv=Process(target=ears.listen_forever,args=())
    plistener.start()
#    plistener.join()
    pcsrv.start()
#    pcsrv.join()
