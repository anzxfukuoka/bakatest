def crypt(txt, step = 10):
    try:
        i = 0
        for c in txt:
            txt = txt[:i] + chr(ord(c) + step) + txt[i+1:]
            i = i + 1
        return txt
    except Exception as e:
        return "err: " + str(e)


def uncrypt(txt, step = 10):
    try:
        i = 0
        for c in txt:
            txt = txt[:i] + chr(ord(c) - step) + txt[i+1:]
            i = i + 1
        return txt
    except Exception as e:
        return "err: " + str(e)
