import sys
import numpy
import os

Filenames = []
unk0 = []

with open("%s_filenames.txt" % (sys.argv[1][:-4]), 'r', encoding="UTF-8") as f:
    Filenames = [line.strip("\r\n").strip("\n").split("\t", -1)[0] for line in f]

file = open(sys.argv[1], "rb")
header_size = numpy.fromfile(file, dtype=numpy.int32, count=1)[0]
file_count = numpy.fromfile(file, dtype=numpy.int32, count=1)[0]
unk2_int32 = numpy.fromfile(file, dtype=numpy.int32, count=1)[0]
round_to = numpy.fromfile(file, dtype=numpy.int32, count=1)[0]
file.seek(0,0)

if (file_count != len(Filenames)): raise ValueError("file_count doesn't match. Expected: %d, got from chapternames.txt: %d" % (file_count, len(Filenames)))

if (len(sys.argv) == 3):
    new_file = open("%s" % (sys.argv[2]), "wb")
else:
    new_file = open("%s_NEW.PAK" % (sys.argv[1][:-4]), "wb")
new_file.write(file.read(0x2C))

scripts_size = []

for i in range(0, file_count):
    script = open("%s\%s.dat" % (sys.argv[1][:-4], Filenames[i]), "rb")
    script.seek(0, 2)
    scripts_size.append(script.tell())
    script.close()

offset = header_size / round_to

for i in range(0, file_count):
    new_file.write(numpy.uint32(offset))
    new_file.write(numpy.uint32(scripts_size[i]))
    offset += int(round((scripts_size[i]+(round_to/2-1)) / round_to))

for i in range(0, file_count):
    new_file.write(Filenames[i].encode("UTF-8"))
    new_file.write(b"\x00")

while(True):
    if (new_file.tell() == header_size): break
    new_file.write(b"\x00")

for i in range(0, file_count):
    script = open("%s\%s.dat" % (sys.argv[1][:-4], Filenames[i]), "rb")
    temp = script.read()
    new_file.write(temp)
    if (len(temp) != (round_to * round((scripts_size[i]+(round_to/2-1)) / round_to))):
        rest = (round_to * round((scripts_size[i]+(round_to/2-1)) / round_to) - len(temp))
        for i in range(0, rest):
            new_file.write(b"\x00")

if (new_file.tell() % 16 != 0):
    rest = 16 - (new_file.tell() % 16)
    for i in range(0, rest):
        new_file.write(b"\x00")