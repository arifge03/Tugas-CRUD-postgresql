import psycopg2 as db
import os

con = None
connected = None
cursor = None

def connect():
    global connected
    global con
    global cursor
    try:
        con = db.connect(
        host = 'localhost', 
        database ="postgres",
        port = 5433,
        user = "gunawan",
        password = "123"
        )
        cursor = con.cursor()
        connected = True
    except:
        connected = False
    return cursor

def disconnect():
    global connected
    global con
    global cursor
    if (connected == True):
        cursor.close()
        con.close()
    else:
        con = None
        connected = False

def Buat():
    global connected
    global con
    global cursor
    a = connect()
    a.execute("""
                CREATE TABLE dosen
                (
                    iddosen serial primary key,
                    nidn varchar(15) unique not null,
                    nama varchar(40) not null,
                    idfakultas integer not null,
                    idprodi integer not null
                    )
                    """)
    con.commit()
    print("Selamat Anda Telah Berhasil Membuat Tabel...")
    
def Entry():
    global connected
    global con
    global cursor
    xnidn = input("Masukan NIDN : ")
    xnama = input("Masukan Nama Lengkap : ")
    xidfk = input("Masukan ID FAKULTAS (1 .. 5) : ")
    xidpr = input("Masukan ID Prodi (1 .. 10) : ")
    a = connect()
    sql = "insert into dosen (nidn, nama, idfakultas, idprodi) values ('"+xnidn+"', '"+xnama+"', '"+xidfk+"', '"+xidpr+"')" 
    a.execute(sql)
    con.commit()
    print("Entry is done.")
    
def Cari():
    global connected
    global con
    global cursor
    xnidn = input("Masukan NIDN yang di cari : ")
    a = connect()
    sql = "select * from dosen where nidn='"+xnidn+"'"
    a.execute(sql)
    record = a.fetchall()
    print(record)
    print("Search is done.")
    
def Ubah():
    global connected
    global con
    global cursor
    xnidn = input("Masukan NIDN yang di cari : ")
    a = connect()
    sql = "select * from dosen where nidn='"+xnidn+"'"
    a.execute(sql)
    record = a.fetchall()
    print("Data saat ini")
    print(record)
    row = a.rowcount
    if (row == 1):
        print("Silakan untuk mengubah data..")
        xnama = input("Masukan Nama Lengkap : ")
        xidfk = input("Masukan ID FAKULTAS (1 - 5) : ")
        xidpr = input("Masukan ID Prodi (1 - 10) : ")
        a = connect()
        sql = "update dosen set nama='"+xnama+"', idfakultas='"+xidfk+"', idprodi='"+xidpr+"' where nidn='"+xnidn+"'" 
        a.execute(sql)
        con.commit()
        print("Update is done.")
        sql = "select * from dosen where nidn='"+xnidn+"'"
        a.execute(sql)
        record = a.fetchall()
        print("Data setelah di ubah :")
        print(record)
    else:
        print("Data tidak di temukan")
        
def Hapus():
    global connected
    global con
    global cursor
    xnidn = input("Masukkan NIDN yang dicari : ")
    a = connect()
    sql = "select * from dosen where nidn ='"+xnidn+"'"
    a.execute(sql)
    record = a.fetchall()
    print("Data saat ini : ")
    print(record)
    row = a.rowcount
    if(row==1):
        jwb=input("Apakah anda ingin menghapus data? (y/t) > > > ")
        if(jwb.upper()=="Y"):
            a = connect()
            sql = "delete from dosen where nidn ='"+xnidn+"'"
            a.execute(sql)
            con.commit()
            print("Delete is done.")
        else:
            print("Data batal untuk dihapus.")
    else:
        print("Data tidak ditemukan")

def show_menu():
  print("\n--- APLIKASI DATABASE POSTGRESQL PYTHON ---")
  print("1. Membuat Tabel Dosen")
  print("2. Buat Data")
  print("3. Cari Data")
  print("4. Ubah Data")
  print("5. Hapus Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")
  os.system("cls")
  if menu == "1":
    Buat()
  elif menu == "2":
    Entry()
  elif menu == "3":
    Cari()
  elif menu == "4":
    Ubah()
  elif menu == "5":
    Hapus()
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")
if __name__ == "__main__":
  while(True):
    show_menu()