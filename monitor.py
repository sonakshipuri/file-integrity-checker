import os, time
from hasher import get_hash
from utils import log

def monitor(folder):
    prev={}
    while True:
        for name in os.listdir(folder):
            path=os.path.join(folder,name)
            if os.path.isfile(path):
                h,_=get_hash(path)
                if path in prev and prev[path]!=h:
                    log(f'Changed: {path}')
                    print('Changed:', path)
                prev[path]=h
        time.sleep(5)