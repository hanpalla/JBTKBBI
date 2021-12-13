from .system import *

def register():
    with open("database.txt", "r") as db:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        confirm = input("Konfirmasi password: ")
        username1 = []
        password1 = []

        for i in db:
            a, b = i.split(",")
            b = b.strip()
            username1.append(a)
            password1.append(b)
       
        if password != confirm:
            print("Password tidak sesuai")
        else:
            if len(password) <= 6:
                print("Password terlalu pendek") 
            elif username in username1:
                print("Akun sudah terdaftar")
            else:
                db = open("database.txt", "a")
                db.write(username + "," + password + "\n")
                print('Success!')
                return
        register()

def access():
    with open("database.txt", "r") as db:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if not len(username or password) < 1:
            username1 = []
            password1 = []
            for i in db:
                a, b = i.split(",")
                b = b.strip()
                username1.append(a)
                password1.append(b)
            data = dict(zip(username1, password1))
            try:
                if data[username]:
                    try:
                        if password == data[username]:
                            print("Login Success")
                            print("Hai, ", username)
                            pause()
                        else:
                            print("Password atau Username anda salah") 
                    except:
                        print("Terjadi kesalahan")
                else:
                    print("username tidak terdaftar")
            except:
                print("Login Eror")
                print("Anda belum memiliki akun, silahkan Signup terlebih dahulu ")
            home()
            
def home():
    clear()
    option = int(input("1.Login | 2.Signup: "))
    if option == 1:
        access()
    elif option == 2:
        register()
    else:
        print("please, enter an option")