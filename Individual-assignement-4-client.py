# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:52:01 2018

@author: tancr
"""
#%%


graph = {
        "a":["b","c"],
        "b":{"d"},
        "c":{"d"},
        "d":{},
        "e":{}        
}

import requests

local_host = 'http://127.0.0.1:5000/{}'

def upload_graph(graph): 
    data = graph
    request = requests.post("http://127.0.0.1:5000/upload_graph/{}".format(graph), json=data)
    if request.status_code == 200:
        return request.json()
    else:
        return request.status_code  



def get_degrees_of_separation(start, end, graph): 
    data = graph
    request = requests.put('http://127.0.0.1:5000/degrees-of-separation/{}/{}'.format(start, end) , json=data)
    if request.status_code == 200:
        return request.json()
    else:
        return request.status_code  
    