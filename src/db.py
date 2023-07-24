import os
from contextlib import contextmanager
from psycopg2 import pool
from logger import logger as log

db_pool = pool.SimpleConnectionPool(1, 10,
                                    host=os.environ["PG_HOST"],
                                    database=os.environ["PG_DB"],
                                    user=os.environ["PG_USER"],
                                    password=os.environ["PG_PASS"],
                                    port=int(os.environ["PG_PORT"]))


@contextmanager
def db():
    con = db_pool.getconn()
    cur = con.cursor()
    try:
        yield con, cur
    finally:
        cur.close()
        db_pool.putconn(con)


def get_minutes_on():
    with db() as (conn, cursor):
        try:
            cursor.execute("""
            select extract(epoch from (status_1 - status_0)) / 60 from (select (
                select max(date)
                from status
                where status = 1
            ) status_1,
            (
                select max(date)
                from status
                where status = 0
            ) status_0) sq
            """)
            result = cursor.fetchall()
            return result[0][0]
        except Exception as e:
            print(str(e))


def get_last_setted():
    with db() as (conn, cursor):
        try:
            cursor.execute(
                "SELECT setted FROM setted order by date desc LIMIT 1")
            result = cursor.fetchall()
            return int(result[0][0])
        except Exception as e:
            log.error(str(e))


def get_last_mode():
    with db() as (conn, cursor):
        try:
            cursor.execute("SELECT mode FROM mode order by date desc LIMIT 1")
            result = cursor.fetchall()
            return result[0][0]
        except Exception as e:
            log.error(str(e))
