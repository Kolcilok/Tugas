import pymysql


con = pymysql.connect(db='coba', user='root', passwd='',
                      host='localhost', port=3306, autocommit=True)
cur = con.cursor()
if cur:
    print("Koneksi terhubung")
else:
    print("Koneksi database gagal")
