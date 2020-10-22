import requests
import json
import mysql.connector


def loginValidationCheck(username, pwd):

    try:
        conn = mysql.connector.connect(
        host ="localhost",
        user = "root",
        password = "ppp",
        database = "db_grad_cs_1917")

        
        cur = conn.cursor(prepared=True)

        sql_cred_query = """ SELECT COUNT(*) FROM users WHERE user_id = %s AND user_pwd=%s;"""
        
        data_tuple = (username, pwd)
        print(data_tuple)
        print(type(data_tuple[0]))
        cur.execute(sql_cred_query, data_tuple)
        result = cur.fetchone()[0]
        print(result)
        if result == 1:
            print("Employee found!")
        else:
            print("emplyoee not found")
        return result
        
    except mysql.connector.Error as error:
        print("parameterizer query failed {}".format(error))

    finally:
        if (conn.is_connected()):
            cur.close()
            conn.close()
            print("Mysql connection closed")


loginValidationCheck("alison", "gradprog2016@07")