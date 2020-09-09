import pymssql
from config.config import *


def get_db_conn():
    conn = pymssql.connect(host=db_host,
                           port=db_port,
                           user=db_user,
                           password=db_password,
                           database=db,
                           charset='utf8'
                           )
    return conn


def query_db(sql):
    conn = get_db_conn()
    cur = conn.cursor()
    logging.debug(sql)
    cur.execute(sql)
    result = cur.fetchall()
    logging.debug(result)
    cur.close()
    conn.close()
    return result


def change_db(sql):
    conn = get_db_conn()
    cur = conn.cursor()
    logging.debug(sql)
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        logging.error(str(e))
    finally:
        cur.close()
        conn.close()


def select_company(name):
    sql = "select customsclearancemodel,* from company"
    result = query_db(sql)
    return True if result else False


def update_company(code):
    sql = "update company set customsclearancemodel = '{}'".format(code)
    change_db(sql)

# def del_user(name):
#     sql = "delete from user where name='{}'".format(name)
#     change_db(sql)
