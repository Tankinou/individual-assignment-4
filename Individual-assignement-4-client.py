# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:52:01 2018

@author: tancr
"""

#2. 5 points. Create an HTTP server and HTTP client to manage a
#phonebook. There should exist the following operations in the phonebook:
#• add a contact (phone + name)
#• get a phone by name
#• delete a phone by name
#• update a phone by name
#Make sure you use JSON to communicate between client and server.


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
    request = requests.post(local_host.format('upload-graph'), json=data)
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
    