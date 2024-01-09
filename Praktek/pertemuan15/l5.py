
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

sql = "SELECT * FROM tabelku"
tampilkan = cur.execute(sql)
hasil = cur.fetchall()
if tampilkan:
    print("data berhasil ditampilkan")

else:
    print("data gagal ditampilkan")
for data in hasil:
    print(data)
