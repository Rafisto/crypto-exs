### Crypto Challenges

1. `mod-ari` [Modular arithmetic - pairs of numbers](./mod-ari/challenge/README.md)
    <details>
    <summary>solution</summary>
    
    In this challenge, our objective is to decode a flag that has been encoded using pairs of integers. The given information includes two lists: `a_i` representing the residues and `m_i` representing the corresponding moduli. The flag is encoded in the form `FLAG{?????_???_?????}`.
    
    The provided Python solution employs the Chinese Remainder Theorem (CRT) to decipher the flag from the given residues and moduli. Let's break down the steps of the solution:
    
    ### Chinese Remainder Theorem (CRT)
    The Chinese Remainder Theorem is a mathematical technique that allows us to find a solution to a system of simultaneous modular congruences. In this case, it is applied to the pairs of integers (`a_i`, `m_i`).
    
    The CRT algorithm involves the following steps:
    1. Calculate the product of all moduli (`prod`).
       2. For each pair (`n_i`, `a_i`), calculate `p` as `prod` divided by `n_i`.
       3. Accumulate the sum of `a_i * mul_inv(p, n_i) * p` for each pair.
       4. Return the final result modulo `prod`.
    
    ### Modular Inverse
    The `mul_inv` function calculates the modular inverse of an integer `a` with respect to a modulus `b`. It is a crucial part of the CRT algorithm. This function ensures that the modular inverse is computed correctly for each modulus in the system.
    
    ### Flag Decoding
    After applying the CRT, the resulting integer is converted back to bytes using `int.to_bytes`. The size of the output is determined by the bit length of the integer. Finally, the decoded flag is printed.
    
    ### Challenge Input
    The challenge provides two lists:
    ```python
    a_i = [1890, 923943128, 9700140639, 30034828954, 81893600223, 7453544462]
    m_i = [2137, 1000000007, 10000000019, 100000000003, 100000000019, 100000000057]
    ```
    
    ### Challenge Output
    The provided Python solution outputs the decoded flag in integer and byte formats.
    
    ### Solution Code
    ```python
    from functools import reduce
    
    
    def chinese_remainder_theorem(m, a):
        sum = 0
        prod = reduce(lambda acc, b: acc * b, m)
        for n_i, a_i in zip(m, a):
            p = prod // n_i
            sum += a_i * mul_inv(p, n_i) * p
        return sum % prod
    
    
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1
    
    
    residues = [1890, 923943128, 9700140639, 30034828954, 81893600223, 7453544462]
    primes = [2137, 1000000007, 10000000019, 100000000003, 100000000019, 100000000057]
    flag_int = chinese_remainder_theorem(primes, residues)
    print(flag_int)
    print(int.to_bytes(flag_int, (flag_int.bit_length() + 7) // 8, 'big'))
    ```
    
    By running the provided code, the flag will be decoded and printed in the required format: `FLAG{?????_???_?????}`.
    </details>

2. `object-dec` [Pwn the `caesar` group member](./object-dec/challenge/README.md)
    <details>
    <summary>solution</summary>
    In this challenge, we have intercepted a poorly encrypted JSON containing credentials of a hacker group named `caesar`. The objective is to decrypt the given encrypted string using a Caesar cipher and extract the flag. The encrypted string is provided, and the flag format is `FLAG{????_??_???????????}`.
    
    ### Caesar Cipher Decryption
    The provided Python solution utilizes a simple Caesar cipher decryption function (`rot13`). The `rot13` function shifts each character by 13 positions in the alphabet. It is applied to both lowercase and uppercase letters, leaving other characters unchanged.
    
    ### Challenge Input
    The encrypted string:
    ```python
    encrypted = "rlW1p2IlozSgMFV6VaOupTS5LGVkZmpvYPNvpTSmp3qipzDvBvNvExkOE3gdpmOhK2ymK3OlMJEcL3EuLzkysFW9"
    ```
    
    ### Challenge Output
    The expected output is the decrypted string in base64 encoding, which is then decoded to reveal the flag in the format `FLAG{????_??_???????????}`.
    
    ### Solution Code
    ```python
    import base64
    
    def rot13(s):
        # Implementation of Caesar cipher (ROT13)
    
    encrypted = "rlW1p2IlozSgMFV6VaOupTS5LGVkZmpvYPNvpTSmp3qipzDvBvNvExkOE3gdpmOhK2ymK3OlMJEcL3EuLzkysFW9"
    
    # Decrypt the Caesar cipher and decode from base64
    decrypted_bytes = base64.b64decode(rot13(encrypted))
    
    # Print the decrypted flag
    print(decrypted_bytes)
    ```
    
    ### Flag Decryption
    Running the provided code will print the decrypted bytes, which, when decoded from base64, will reveal the flag in the specified format.
    
    ### Note
    The Caesar cipher is a basic encryption technique, and the ROT13 variant is a special case where the shift is 13 positions. This type of cipher is relatively easy to break, and more secure encryption methods should be used for sensitive information in real-world scenarios.
    </details>
3. `xor-img` [When one time pad is used two times](./xor-img/challenge/README.md)
    <details>
    <summary>solution</summary>
    In this challenge, the target has XOR-encrypted two images using a single cipher. The goal is to retrieve the flag, which is expected to be in the format `FLAG{?????????}`. The provided solution uses Python and the Python Imaging Library (PIL) to decrypt the images.
    
    ### XOR Cipher Decryption on Images
    The XOR cipher is a bitwise operation that is often used for encryption. In this scenario, the solution XOR-decrypts each pixel of the two images (`enc1.png` and `enc2.png`) to reveal the original image. The decrypted image is then saved as `dec.png`.
    
    ### Challenge Input
    Two encrypted images: `enc1.png` and `enc2.png`
    
    ### Challenge Output
    The expected output is the decrypted image saved as `dec.png`, and the flag in the format `FLAG{?????????}`.
    
    ### Solution Code
    ```python
    from PIL import Image
    
    # Open the two encrypted images
    enc1 = Image.open('./enc1.png')
    enc2 = Image.open('./enc2.png')
    
    # Get the dimensions of the images
    width, height = enc1.size
    
    # Load pixel data for each image
    enc1_pixel = enc1.load()
    enc2_pixel = enc2.load()
    
    # Create a new image for the decrypted result
    res_dec = Image.new("RGB", (width, height))
    dec_pixel = res_dec.load()
    
    # XOR-decrypt each pixel and store the result
    for y in range(height):
        for x in range(width):
            enc1_r, enc1_g, enc1_b = [int(k) for k in enc1_pixel[x, y]]
            enc2_r, enc2_g, enc2_b = [int(k) for k in enc2_pixel[x, y]]
            dec_pixel[x, y] = enc1_r ^ enc2_r, enc1_g ^ enc2_g, enc1_b ^ enc2_b
    
    # Save the decrypted image
    res_dec.save('./dec.png')
    ```
    
    ### Flag Retrieval
    The decrypted image (`dec.png`) can be viewed, and the flag should be extracted from the image.
    
    ### Note
    XOR encryption is a simple bitwise operation, and its security is limited. It's used here for educational purposes, and in real-world scenarios, more robust encryption methods should be employed for securing sensitive information.
    </details>