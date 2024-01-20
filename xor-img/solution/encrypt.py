from random import randint

from PIL import Image

donald = Image.open('./donald.png')
flag = Image.open('./flag.png')
width, height = donald.size

donald_pixel = donald.load()
flag_pixel = flag.load()

donald_enc = Image.new("RGB", (width, height))
flag_enc = Image.new("RGB", (width, height))

donald_enc_pixel = donald_enc.load()
flag_enc_pixel = flag_enc.load()

for y in range(height):
    for x in range(width):
        donald_r, donald_g, donald_b = [int(k) for k in donald_pixel[x, y]]
        flag_r, flag_g, flag_b = [int(k) for k in flag_pixel[x, y]]
        rand_r, rand_g, rand_b = randint(0, 255), randint(0, 255), randint(0, 255)
        donald_enc_pixel[x, y] = donald_r ^ rand_r, donald_g ^ rand_g, donald_b ^ rand_b
        flag_enc_pixel[x, y] = flag_r ^ flag_r, flag_g ^ rand_g, donald_b ^ rand_b

donald.close()
flag.close()

donald_enc.save('./enc1.png')
flag_enc.save('./enc2.png')
