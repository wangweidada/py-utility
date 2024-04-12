import MySQLdb as mdb
import logging
logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(module)s/%(funcName)s:%(message)s',
                        datefmt='%Y-%m-%d-%X')
class GetDbData:
    def __init__(self,host,name,pw,db,port=3306):
        self.host = host
        self.name = name
        self.pw = pw
        self.db = db
        self.port = port
    def connect(self):
        connectResult = 0
        try:
            self.con = mdb.connect(host=self.host,user=self.name,passwd=self.pw,db=self.db,port=self.port,charset="utf8")
            if self.con is not None:
                logging.info('db连接已经建立')
            else:
                logging.info('db连接无法建立')
                connectResult = 1
        except Exception as e:
            connectResult = 1
            logging.info('db连接出现问题，{}'.format(e))
        return connectResult
    def excuteSql(self,sql):
        try:
            connect = self.connect()
            if connect == 0:
                cur = self.con.cursor()
                # 创建一个数据表 writers(id,name)
                cur.execute(sql)
                rows = cur.fetchall()
            else:
                logging.info('db连接出问题，该sql不能执行!')
                rows = None
        except Exception as e:
            rows = None
            logging.info('something wrong happened:{}'.format(e))
        finally:
            if hasattr(self,'con') is True:
                self.con.close()
                logging.info('db连接已经关闭')
            else:
                logging.info('由于连接不存在，db无需关闭连接')
        logging.info('sql执行结果返回')
        return rows

    def excuteManySql(self,sqls):
        results = []
        try:
            connect = self.connect()
            if connect == 0:
                cur = self.con.cursor()
                for sql in sqls:
                    cur.execute(sql)
                    rows = cur.fetchall()
                    results.append(rows)
            else:
                logging.info('db连接出问题，该sql不能执行!')
                rows = None
        except Exception as e:
            rows = None
            logging.info('something wrong happened:{}'.format(e))
        finally:
            if hasattr(self,'con') is True:
                self.con.close()
                logging.info('db连接已经关闭')
            else:
                logging.info('由于连接不存在，db无需关闭连接')
        logging.info('sql执行结果返回')
        return results
    def excuteSqlWithout(self,sql):
        try:
            cur = self.con.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
        except Exception as e:
            rows = None
            logging.info('something wrong happened:{}'.format(e))
        logging.info('sql执行结果返回')
        return rows
    def close(self):
        if hasattr(self, 'con') is True:
            self.con.close()
            logging.info('db连接已经关闭')
        else:
            logging.info('由于连接不存在，db无需关闭连接')

    def updateOneSql(self,sql):
        r1 = 0
        try:
            connect = self.connect()
            if connect == 0:
                cur = self.con.cursor()
                r1 = cur.execute(sql)
                self.con.commit()
            else:
                print('db连接出问题，该sql不能执行!')
        except Exception as e:

            print('something wrong happened:{}'.format(e))
        finally:
            if hasattr(self,'con') is True:
                self.con.close()
                print('db连接已经关闭')
            else:
                print('由于连接不存在，db无需关闭连接')
        print(f'该修改sql语句影响：{r1}行')
        return r1
    def updateSqls(self,sqls,batch):
        group = len(sqls)/batch
        if group * batch < len(self):
            group += 1
        for i in range(group):
            sqlsOneBatch = sqls[i*batch:(i+1)*batch]
            self.updateOneSqlsBatch(sqlsOneBatch)
    def updateOneSqlsBatch(self,sqls):
        try:
            connect = self.connect()
            if connect == 0:
                cur = self.con.cursor()
                for i in sqls:
                    cur.execute(i)
                self.con.commit()
            else:
                print('db连接出问题，该sql不能执行!')
        except Exception as e:

            print('something wrong happened:{}'.format(e))
        finally:
            if hasattr(self,'con') is True:
                self.con.close()
                print('db连接已经关闭')
            else:
                print('由于连接不存在，db无需关闭连接')
        print('sql执行结果返回')