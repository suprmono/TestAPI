import pymssql


class DB:
    def __init__(self):
        self.conn = pymssql.connect(server='127.0.0.1',
                                    port=1433,
                                    username='sa',
                                    password='123',
                                    database='cmp',
                                    charset='utf8'
                                    )
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def select_company(self, name):
        result = self.query("select customsclearancemodel,* from company where tradename='{}'".format(name))
        return True if result else False

    def update_company(self, code):
        self.exec("update company set customsclearancemodel = '{}'".format(code))


if __name__ == '__main__':
    db = DB()
    if db.select_company('深圳市祺腾实业有限公司'):
        db.update_company('1')
