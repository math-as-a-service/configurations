#!/usr/bin/env python3

import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
)

with connection.cursor() as cursor:
    cursor.execute('CREATE DATABASE IF NOT EXISTS maas')
    cursor.execute("GRANT ALL ON `maas`.* TO 'maas_user'@'localhost' IDENTIFIED BY 'maas_password'")
