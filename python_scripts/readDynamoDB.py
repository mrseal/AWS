import boto3
import time
from threading import Thread

def read(table, times):
    ct = 0
    while ct < times:
        ct += 1
        table.get_item(Key={'key':'value'})

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TableName')

threadNum = 100
readTimesPerThread = 1000

try:
    count = 0
    while count < threadNum:
        count += 1
        t = Thread(target=read, args=(table, readTimesPerThread,))
        t.start()
except:
    print("Thread Error!")



