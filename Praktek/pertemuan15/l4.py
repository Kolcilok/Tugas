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
sql = """INSERT INTO tabelku (id, nama, email) VALUES (3, 'Cinta', 'cinta@gmail.com')"""
inserttabel = cur.execute(sql)
con.commit()
if inserttabel:

    print("data berhasil disisipkan")

else:

    print("data gagal disisipkan")
