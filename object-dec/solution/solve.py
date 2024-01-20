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


encrypted = "rlW1p2IlozSgMFV6VaOupTS5LGVkZmpvYPNvpTSmp3qipzDvBvNvExkOE3gdpmOhK2ymK3OlMJEcL3EuLzkysFW9"

print(base64.b64decode(rot13(encrypted)))
