from frame.db import Db
from frame.error import ErrorCode
from frame.sql import Sql
from frame.value import Udata


class UdataDb(Db):

    def insert(self,id, schooltype, majorcate, age, intern, toeic, tosp, train, jobseek, cert, jobsearch, yrwish, wishhr, wishsalary, jobgradu, liveexp):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.udatainsert % (id, schooltype, majorcate, age, intern, toeic, tosp, train, jobseek, cert, jobsearch, yrwish, wishhr, wishsalary, jobgradu, liveexp));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor, conn);
    def delete(self,id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.udatadelete % (id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor,conn);
    def update(self,id, schooltype, majorcate, age, intern, toeic, tosp, train, jobseek, cert, jobsearch, yrwish, wishhr, wishsalary, jobgradu, liveexp):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.udataupdate % (schooltype, majorcate, age, intern, toeic, tosp, train, jobseek, cert, jobsearch, yrwish, wishhr, wishsalary, jobgradu, liveexp, id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor,conn);
    def selectone(self,id):
        udata = None;
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.udatalistone % id);
        c = cursor.fetchone();
        udata = Udata(c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9],c[10],c[11],c[12],c[13],c[14],c[15],c[16],c[17]);
        super().close(cursor,conn);
        return udata;

    def select(self):
        all = [];
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.udatalist);
        result = cursor.fetchall();
        for c in result:
            udata = Udata(c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9],c[10],c[11],c[12],c[13],c[14],c[15],c[16],c[17]);
            all.append(udata);
        super().close(cursor,conn);
        return all;

    def selectall(self,id):
        all = [];
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.udatalistone % id);
        result = cursor.fetchall();
        for c in result:
            udata = Udata(c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9],c[10],c[11],c[12],c[13],c[14],c[15],c[16],c[17]);
            all.append(udata);
        super().close(cursor,conn);
        return all;


if __name__ == '__main__':
    UdataDb().insert('hakdj',1,1,23,0,900,0,0,1,0,2,2,0,0,2,1);

    # result=UdataDb().select();
    # for r in result:
    #     print(r);
    #
    # try:
    #     UdataDb().update('id04',1,1,23,0,800,0,0,1,0,2,2,0,0,2,1);
    #     print('OK');
    # except:
    #     print(ErrorCode.e0001);
    # #
    # result=UdataDb().selectone('hakdj');
    # print(result);

    # UdataDb().delete('hakdj')