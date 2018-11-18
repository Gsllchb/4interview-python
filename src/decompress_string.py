"""Google Former Coding Interview Question: Compression and Decompression
https://techdevguide.withgoogle.com/paths/advanced/compress-decompression/#!"""


def decompress(str):
    if str.isalpha():
        return str
    result = ''
    stack = 0
    num = 0
    substr = ''
    for c in str:
        if stack == 0:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == '[':
                stack += 1
            else:
                result += c
        else:
            if c == '[':
                stack += 1
            elif c == ']':
                stack -= 1
            if stack == 0:
                result += num * decompress(substr)
                num = 0
                substr = ''
            else:
                substr += c
    return result
