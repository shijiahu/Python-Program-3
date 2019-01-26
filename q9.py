# 9. Question:
# Please write a program to compress and decompress the 
# string "hello world!hello world!hello world!hello world!".
# Hints:
# Use zlib.compress() and zlib.decompress() to compress and decompress a string.

import zlib

data = 'hello world!hello world!hello world!hello world!'
compressed_data = zlib.compress(data.encode("utf-8"))
print(compressed_data)
decompressed_data = zlib.decompress(compressed_data)
print(decompressed_data)