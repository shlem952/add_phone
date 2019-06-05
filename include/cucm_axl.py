from suds.client import Client
from suds.xsd.doctor import Import
from suds.xsd.doctor import ImportDoctor
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import config

wsdl = config.wsdl
cucm_url = config.cucm_url
username = config.username
password = config.password

tns = 'http://schemas.cisco.com/ast/soap/'
imp = Import('http://schemas.xmlsoap.org/soap/encoding/',
             'http://schemas.xmlsoap.org/soap/encoding/')
imp.filter.add(tns)


def connect_to_cucm():
    client = Client(wsdl,location=cucm_url,faults=False,plugins=[ImportDoctor(imp)],
                username=username,password=password)
    return client


if __name__ == "__main__":
    pass