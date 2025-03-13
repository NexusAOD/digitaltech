import pymysql

def get_connection() -> pymysql.connections.Connection:
    return pymysql.connect(host='127.0.0.1', user='root', password='kraken123', db='digital_tech', port=3306)