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
sql = "UPDATE tabelku SET nama=%s,email=%s WHERE id=%s"
val = ("Budiku", "Budiku@gmail.com", 3)
updatedata = cur.execute(sql, val)
if updatedata:
    print("data berhasil diperbarui")
else:
    print("data gagal diperbarui")
