import json
import pymysql
import time
import os
from datetime import datetime



host        = os.environ["DB_HOST"]
user        = os.environ["DB_USERNAME"]
password    = os.environ["DB_PASSWORD"] 
db          = os.environ["DB_NAME"]

def make_path(student_id, lecture_name):
    path = f"qrcodes/{student_id}/{lecture_name}/qrcode.jpg"
    return path

    
def lambda_handler(event, context):
    connect     = pymysql.connect(host =host, user=user, password = password, port = 3306, db = db)
    cursor = connect.cursor()
   
    
    inc = event.get('inc')
    sen_id = event.get('sen_id')
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # sql = f"INSERT INTO inclination VALUES ('1','roger','{time}');"
    # print(sql)
    # cursor.execute(sql)
    # connect.commit()
    
    
    
    if inc and sen_id:
        sql = f"INSERT INTO inclination VALUES ('{inc}','{sen_id}','{time}');"
        print(sql)
        cursor.execute(sql)
        connect.commit()
    else:
        return print(event,"값을 받아올 수 없습니다")
        
    if not cursor.fetchall():
        
        return print(f"구문실행오류!!! 값:{cursor.fetchall()}")
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

