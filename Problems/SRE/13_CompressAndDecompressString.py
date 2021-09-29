import sys
import zlib


def compress_and_decompress(text):

    # Checking the size of original text
    text_size = sys.getsizeof(text)
    print('Size of original text: ', text_size)

    # Checking the size of compressed text
    compressed = zlib.compress(text)
    csize = sys.getsizeof(compressed)
    print('Size of compressed text: ', csize)

    # Checking the size of decompressed text
    decompressed = zlib.decompress(compressed)
    dsize = sys.getsizeof(decompressed)
    print('Size of decompressed text: ', dsize)

    # Difference between compressed and decompressed
    print('Difference between compressed and decompressed text: ', text_size-csize)


def main():
    text = b"""This function is the primary interface to this module along with
decompress() function. This function returns byte object by compressing the data
given to it as parameter. The function has another parameter called level which
controls the extent of compression. It an integer between 0 to 9. Lowest value 0
stands for no compression and 9 stands for best compression. Higher the level of
compression, greater the length of compressed byte object."""

    compress_and_decompress(text)


if __name__ == '__main__':
    main()
