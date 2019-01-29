#!/usr/bin/env python2

data = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x3C, 0x3C, 0x3C, 0x3C, 0x3C, 0x3C, 0x3C, 0x3C, 0x3C, 0x3C, 0x60, 0x60, 0x60, 0x60, 0x60, 0x60, 0x7E, 0x7E, 0x7E, 0x7E, 0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0x7E, 0x7E, 0x7E, 0x7E, 0x60, 0x60, 0x7E, 0x7E, 0x7E, 0x7E, 0x60, 0x60, 0x7E, 0x7E, 0x7E, 0x7E, 0x7E, 0x7E, 0x7E, 0x7E, 0x62, 0x62, 0x66, 0x66, 0x7E, 0x7E, 0x78, 0x78, 0x6C, 0x6C, 0x6E, 0x6E, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x80, 0x80, 0xFF, 0xFF, 0xFF, 0xFF, 0x01, 0x01, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xC1, 0xC1, 0xFF, 0xFF, 0xFF, 0xFF, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0x7E, 0x7E, 0xFF, 0xFF, 0xC3, 0xC3, 0xC3, 0xC3, 0xC3, 0xC3, 0xC3, 0xC3, 0xFF, 0xFF, 0x7E, 0x7E, 0xC3, 0xC3, 0xE3, 0xE3, 0xF3, 0xF3, 0xFB, 0xFB, 0xDF, 0xDF, 0xCF, 0xCF, 0xC7, 0xC7, 0xC3, 0xC3, 0xFF, 0xFF, 0xFF, 0xFF, 0xC0, 0xC0, 0xFF, 0xFF, 0xFF, 0xFF, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xFF, 0xFF, 0xFF, 0xFF, 0x3C, 0x3C, 0x7E, 0x7E, 0xC3, 0xC3, 0xC3, 0xC3, 0xFF, 0xFF, 0xFF, 0xFF, 0xC3, 0xC3, 0xC3, 0xC3, 0xFE, 0xFE, 0xFE, 0xFE, 0xC6, 0xC6, 0xC0, 0xC0, 0xDF, 0xDF, 0xC1, 0xC1, 0xFF, 0xFF, 0xFF, 0xFF, 0xF0, 0xF0, 0xF0, 0xF0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xF0, 0xF0, 0xF0, 0xF0, 0x0F, 0x0F, 0x0F, 0x0F, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x0F, 0x0F, 0x0F, 0x0F, 0xFF, 0xFF, 0xFF, 0xFF, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xFF, 0xFF, 0xFF, 0xFF, 0x7E, 0x7E, 0x7E, 0x7E, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x7E, 0x7E, 0x7E, 0x7E, 0x00, 0xFF, 0x00, 0xFF, 0x00, 0xFF, 0x00, 0xFF, 0x00, 0xFF, 0x00, 0xFF, 0x00, 0xFF, 0x00, 0xFF, 0xFE, 0xFE, 0xFE, 0xFE, 0x82, 0x00, 0xEE, 0x6C, 0x82, 0x00, 0xBA, 0x38, 0x00, 0x00, 0x40, 0x00, 0xC3, 0xC3, 0xE3, 0xE3, 0xF3, 0xF3, 0xFB, 0xFB, 0xFF, 0xFF, 0xDF, 0xDF, 0xCF, 0xCF, 0xC7, 0xC7, 0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0xFF, 0xFF, 0x81, 0x81, 0xA5, 0xA5, 0x81, 0x81, 0x7E, 0x7E, 0xFF, 0xFF, 0x81, 0xE7, 0x81, 0xFF, 0x81, 0xDB, 0x81, 0xDB, 0x81, 0xDB, 0x81, 0xC3, 0xFF, 0xFF, 0xFF, 0xFF, 0x81, 0xFF, 0x81, 0xFF, 0x81, 0x99, 0x81, 0x99, 0x81, 0x99, 0x81, 0x99, 0xFF, 0xFF, 0x7E, 0x7E, 0xC3, 0xC3, 0x81, 0x81, 0xFF, 0xFF, 0xA5, 0xA5, 0x81, 0x81, 0xC3, 0xDB, 0x7E, 0x7E, 0x7E, 0x7E, 0xFF, 0xE7, 0xFF, 0xC3, 0xFF, 0xFF, 0xFF, 0xA5, 0xFF, 0x81, 0xE7, 0xDB, 0x7E, 0x7E, 0x1F, 0x1F, 0x31, 0x3F, 0x61, 0x7F, 0xC1, 0xFF, 0xC1, 0xFF, 0x61, 0x7F, 0x3F, 0x3F, 0x1F, 0x1F, 0xFF, 0xFF, 0x9D, 0xE3, 0x8D, 0xF3, 0x85, 0xFB, 0xA1, 0xDF, 0xB1, 0xCF, 0xB9, 0xC7, 0xFF, 0xFF]

tiles = []

for x in xrange(18):
    tiles += [[data[x * 16 + y] for y in range(16)]]

for c in [13, 0,  1,  2, 3, 2, 4, 16, 5, 4, 8, 7, 4, 5, 6, 7, 8]:
    tile = tiles[c]
    for x in tile:
        print ('0'*8 + bin(x)[2:])[-8:].replace('0', ' ').replace('1', 'X')
    print