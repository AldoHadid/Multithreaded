from genericpath import isfile
from msilib.schema import File
from flask import Flask, render_template, safe_join, abort, send_file
import os
import datetime as dt
from pathlib import Path
import socket
import config
from _thread import *
import threading

# create a server
app = Flask(__name__)

host = '127.0.0.1'
port = 50100

baseFolderPath = r'C:\Users\Aldo Hadid\Downloads\drive-download-20221005T124356Z-001'

path = 'C:/Users/Aldo Hadid/Documents/KULIAH/SEMESTER 9 huhu/Progjar/Web Server/Multithreaded_WebServer/'
CRLF = '\r\n'

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(1)
print( '%s is Activated ...' % host)
print('Listening on port %s ...' % port)

def thread(client_connection, client_address):
    print ("Tambak koneksi: ", client_address)

    while True:    
        # Wait for client connections
        client_connection, client_address = server_socket.accept()
        
        # Get the client request
        request = client_connection.recv(1024).decode()

        # get filename
        headers = request.split('\n')
        filename = headers[0].split()[1]
        indexname = filename.replace('/','')
        hostname = headers[1].split(':')[1]
        koneksi = headers[2].split()[1]

        # Config
        if hostname == config.web1:
            Directory = config.pathfinder1
            newdir = os.path.dirname(Directory)
        elif hostname == config.web2:
            Directory = config.pathfinder2
            newdir = os.path.dirname(Directory)
        else:
            Directory = config.Directory
            newdir = os.path.dirname(Directory)

        if filename == '/':
                filename = '/index.html'

                fin = open(Directory + filename)
                content = fin.read()
                fin.close()

                # Send HTTP response
                response = 'HTTP/1.0 200 OK'+CRLF+'Content-Type: text/html'+CRLF*2+ content
                client_connection.sendall(response.encode())
                client_connection.close()

        elif '.' in filename:        
        # Get the content of htdocs/index.html        
            if 'html' in filename:
                fin = open(Directory + filename)
                content = fin.read()
                fin.close()

                # Send HTTP response
                tipe = 'text/html'
                response = 'HTTP/1.0 200 OK'+CRLF+'Content-Type: '+tipe+CRLF*2+ content
                client_connection.sendall(response.encode())
                client_connection.close()

            else:
                with open(Directory+filename, 'rb') as file_to_send:
                        tipe = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                        response = 'HTTP/1.0 200 OK'+CRLF+tipe+CRLF*2
                        client_connection.sendall(response.encode())
                        client_connection.sendfile(file_to_send)
                        client_connection.close()

        print('\n')
        if koneksi != 'keep-alive':
            break

@app.route('/')
def index():
    return "Halo Dunia!!"

def getTimeStampString(tSec: float) -> str:
    tObj = dt.datetime.fromtimestamp(tSec)
    tStr = dt.datetime.strftime(tObj, '%Y-%m-%d %H:%M:%S')
    return tStr

def getReadableByteSize(num, suffix='B') -> str:
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

@app.route('/reports/', defaults = {'reqPath':""})
@app.route('/reports/<path:reqPath>')
def reports(reqPath):
    absPath = safe_join(baseFolderPath, reqPath)

    if not os.path.exists(absPath):
        return abort(404)

    if os.path.isfile(absPath):
        return send_file(absPath)

    def fObjFromScan(x):
        fileStat = x.stat()
        fBytes = getReadableByteSize(fileStat.st_size)
        fTime = getTimeStampString(fileStat.st_mtime)
        return {
                'name': x.name, 
                'size': fBytes, 
                'mTime': fTime,
                'fLink': os.path.relpath(x.path, baseFolderPath)
                }
    fNames = [fObjFromScan(x) for x in os.scandir(absPath)]
    return render_template('files.html.j2', files=fNames)

while True:

    # Wait for client connections
    client_connection, client_address = server_socket.accept()
    # print_lock.acquire()
    start_new_thread(thread, (client_connection,client_address))