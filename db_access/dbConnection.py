import json
import mysql.connector
from mysql.connector import Error
import os,sys,inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, current_dir)
credFile = current_dir + "/credentials.json"

class credentialsDB():
    def __init__(self, h, u, p):
        self.host = h
        self.user = u
        self.psw = p

def getCredentials():
    cF = open(credFile,)
    c = json.load(cF)

    return credentialsDB(h = c['host'], u= c['user'], p = c['psw'])
    
def connectDB():
    cred = None
    try:
        cred = getCredentials()
    except Exception as e: 
        print(e)
        print("Can't access credentials files")
        return

    try:
        mydb = mysql.connector.connect(
          host = cred.host,
          user = cred.user,
          password = cred.psw,
          database = "assettoDB"
        )

        print("MySQL Database connection successful")

        return mydb
        
    except Error as err:
        print(f"Error: '{err}'")

    
