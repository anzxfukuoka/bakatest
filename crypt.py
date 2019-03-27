def crypt(txt, step = 10):
    i = 0
    for c in txt:
        txt = txt[:i] + chr(ord(c) + step) + txt[i+1:]
        i = i + 1
    return txt


def uncrypt(txt, step = 10):
    i = 0
    for c in txt:
        txt = txt[:i] + chr(ord(c) - step) + txt[i+1:]
        i = i + 1
    return txt
