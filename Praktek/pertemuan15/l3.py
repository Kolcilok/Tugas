
import pymysql
con = pymysql.connect(db='dbku', user='root', passwd='',
                      host='localhost', port=3306, autocommit=True)
cur = con.cursor()

if cur:
    print("Koneksi database terhubung")

else:
    print("Koneksi database gagal")

usedb = cur.execute("USE dbku")
if usedb:
    print("database berhasil digunakan")

else:
    print("database gagal digunakan")

sql = """CREATE TABLE tabelku (
id INTEGER (3) NOT NULL PRIMARY KEY, 
nama VARCHAR(25),
email VARCHAR(30)
)"""

buattabel = cur.execute(sql)
if buattabel:
    print("Tabel berhasil dibuat")

else:
    print("Tabel gagal dibuat")
