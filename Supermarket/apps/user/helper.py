import hashlib


#此函数为加密函数
def set_password(pwd):
    h = hashlib.md5(pwd.encode('utf-8'))
    return h.hexdigest()