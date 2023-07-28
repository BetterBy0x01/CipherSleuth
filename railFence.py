def rail_fence_encrypt(plain_text, rails):
    fence = [[' ' for _ in range(len(plain_text))] for _ in range(rails)]
    rail, direction = 0, 1

    for char in plain_text:
        fence[rail][len(fence[rail]) - len(plain_text):] = char
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1

    encrypted_text = ''.join([''.join(row) for row in fence])
    return encrypted_text

def rail_fence_decrypt(encrypted_text, rails):
    fence = [[' ' for _ in range(len(encrypted_text))] for _ in range(rails)]
    rail, direction = 0, 1

    for i in range(len(encrypted_text)):
        fence[rail][i] = '*'
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1

    index = 0
    for i in range(rails):
        for j in range(len(encrypted_text)):
            if fence[i][j] == '*':
                fence[i][j] = encrypted_text[index]
                index += 1

    rail, direction = 0, 1
    decrypted_text = ''
    for _ in range(len(encrypted_text)):
        decrypted_text += fence[rail].pop(0)
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1

    return decrypted_text