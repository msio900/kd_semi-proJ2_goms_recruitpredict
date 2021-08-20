import pymysql;
import json
import os
from pathlib import Path


from django.core.exceptions import ImproperlyConfigured
BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, 'secrets.json')  # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

config = {
    'database': 'goms',
    'user': 'gomuser',
    'password': get_secret("password"),
    'host':'127.0.0.1',
    'port': 3306,
    'charset':'utf8',
    'use_unicode':True
}
class Db:
    def getConnection(self):
        conn = pymysql.connect(**config);
        return conn;

    def close(self, conn, cursor):
        if cursor != None:
            cursor.close();
        if conn != None:
            conn.close();