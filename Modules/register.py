def call(username,pasw,mail):
    f = open("userid.bin",'rb+')
    for i in f:
        if i == username:
            f.close()
            return -1
        v1 = f.readline()
        v2 = f.readline()
    
    f.write(usersname)
    f.write(pasw)
    f.write(mail)
    f.close()
    return 0

def check(username,pasw):
    f = open("userid.bin",'rb+')
    flag = 0
    for i in f:
        if i == username:
            flag = 1
            break
    v1 = f.readline()
    v2 = f.readline()
    if flag == 0:
        f.close()
        return -1

    pas = f.readline()
    if pas == pasw:
        f.close()
        return 0
    else:
        f.close()
        return -1
        