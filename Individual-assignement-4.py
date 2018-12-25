# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 00:02:14 2018

@author: tancr
"""
#%%
#2 Exercises
#In this exercise we will create an HTTP server to which we can upload a
#graph and in which we can get the degrees of separation between two nodes
#in the graph.



from flask import Flask, jsonify, request

server = Flask("IndividualAssignement4")


@server.route('/upload_graph', methods=['POST'])
def upload_graph():
    body = request.get_json()
    return jsonify(body)
    

@server.route('/degrees-of-separation/<start>/<end>', methods=['PUT'])
def find_path(graph = '', start, end, path = []):
    
    
    path = path + [start]    
    
    if start == end:
        return path
    
    if start not in graph:
        return None
    
    for conn in graph[start]:
        
        if conn not in path:
            new_path = find_path(graph, conn, end, path)
            
            if new_path is not None: 
                return new_path 
            
    return None



server.run()


