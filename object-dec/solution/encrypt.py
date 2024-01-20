# FLAG{js0n_is_predictable}
import base64


def rot13(s):
    result = ""
    for v in s:
        c = ord(v)
        if ord('a') <= c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif ord('A') <= c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13
        result += chr(c)
    return result


flag = "FLAG{js0n_is_predictable}"
object = '{"username":"papaya2137", "password": "' + flag + '"}'
cipher = base64.b64encode(object.encode())
print(rot13(str(cipher)))
