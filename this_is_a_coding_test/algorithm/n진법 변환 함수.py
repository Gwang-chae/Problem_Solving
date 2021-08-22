import string

tmp = string.digits + string.ascii_lowercase
def convert(n, base):
    q,r = divmod(n, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]