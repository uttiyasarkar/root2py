import os
#from importlib import resources
CURDIR = os.path.abspath(os.path.curdir)

def get_data():
    filepath = CURDIR+"/data/sample.root"
    return filepath

def save_data(a: str)->str:
    savefile = CURDIR+"/data/"+a
    return savefile

#print(get_data())