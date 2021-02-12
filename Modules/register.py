def call(username,pasw,mail):
    f = open("userid.txt",'r')
    for i in f:
        a = i.split()
        if a[0] == username:
            f.close()
            return -1
        v1 = f.readline()
        v2 = f.readline()
    
    f.close()
    f = open("userid.bin","a")
    f.write(username+'\n')
    f.write(pasw+'\n')
    f.write(mail+'\n')
    f.close()
    return 0

def check(username,pasw):
    f = open("userid.txt",'r')
    flag = 0
    for inp in f:
        a = inp.split()
        if a[0] == username:
            flag = 1
            break
        v = f.readline()
        v2 = f.readline()
    
    if flag == 0:
        f.close()
        return -1

    pas = f.readline()
    pa = pas.split()
    if pa[0] == pasw:
        f.close()
        return 0
    else:
        f.close()
        return -1
     