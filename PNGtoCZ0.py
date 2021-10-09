import png
import sys
import pathlib
import numpy

MAGIC = b"CZ0\x00"
Header_size = 0x200.to_bytes(4, byteorder="little")
BPP = 0x20.to_bytes(2, byteorder="little")
image = png.Reader(file = open(sys.argv[1], "rb"))
width,height,data,_ = image.asRGBA8()

stack = numpy.vstack(map(numpy.uint8, data))

if (len(sys.argv) == 3):
    new_file = open("%s" % (sys.argv[2]), "wb")
else:
    new_file = open("%s.dat" % (pathlib.Path(sys.argv[1]).stem), "wb")
new_file.write(MAGIC)
new_file.write(Header_size)
new_file.write(width.to_bytes(2, byteorder='little'))
new_file.write(height.to_bytes(2, byteorder='little'))
new_file.write(BPP)
new_file.write(b"\x03\x00")
new_file.write(b"\x00\x00\x00\x00")
new_file.write(width.to_bytes(2, byteorder='little'))
new_file.write(height.to_bytes(2, byteorder='little'))
new_file.write(width.to_bytes(2, byteorder='little'))
new_file.write(height.to_bytes(2, byteorder='little'))
while(new_file.tell() < 0x200):
    new_file.write(b"\x00")
new_file.write(stack)