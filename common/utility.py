# -*- coding: utf-8 -*-
from datetime import datetime as dt
from pytz import timezone
import socket

def now_timestamp():
    return dt.now().strftime("%Y-%m-%d %H:%M:%S")

def list_to_bool(l:list):
    bool_list=[]
    for item in l:
        bool_list.append(False if item == "0" or item == 0 else True)
    
    return bool_list

def create_proxy_dict(id,password,host,port,proxy_flg=True):
    if proxy_flg:
        proxy_url=f"http://{id}:{password}@{host}:{port}"
        return {
            "http": proxy_url,
            "https": proxy_url
        }
    else:
        return {}

def get_global_ip():
    return socket.gethostbyname(socket.gethostname())
