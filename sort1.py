# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 22:40:35 2021

@author: USER

a = int(input('a='))
"""

list=[2,6,7,8,12,22,26,29,30,50]
l=0
r=9#
n=29#
while(l<=r):
    m=(l+r)/2
    m=int(m)
    if(list[m]==n):
        ans=m
    elif(list[m]<n):
        l=m+1
    else:
        r=m-1
print(ans)

#Reloaded modules: jupyter_client.session, zmq.eventloop, zmq.eventloop.ioloop,
#tornado.platform, tornado.platform.asyncio, tornado.gen, zmq.eventloop.
#zmqstream, jupyter_client.jsonutil, jupyter_client.adapter, spyder, 
#spyder.pil_patch, PIL, PIL._version, PIL.Image, PIL.ImageMode, PIL.TiffTags,
# PIL._binary, PIL._util, PIL._imaging, cffi, cffi.api, cffi.lock, 
#cffi.error, cffi.model