import pymysql
con = pymysql.connect(db='coba', user='root', passwd='',
                      host='localhost', port=3306, autocommit=True)
cur = con.cursor()
if cur:
    print("Koneksi database terhubung")
else:
    print("Koneksi database gagal")

buatdb = cur.execute("CREATE DATABASE testdb")
if buatdb:
    print("Buat database berhasil")
else:
    print("Buat database gagal")
