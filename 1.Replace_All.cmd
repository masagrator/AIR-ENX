python PNGtoCZ0.py image\PARTS\options_bg.png PAKs\PARTS\options_bg.dat
python PNGtoCZ0.py image\PARTS\options_tab.png PAKs\PARTS\options_tab.dat
python image_repacker.py PAKs\PARTS.PAK atmosphere\contents\0100ADC014DA0000\romfs\image\PARTS.PAK
echo f | xcopy /y movie\AIR_OP_B.webm atmosphere\contents\0100ADC014DA0000\romfs\movie\AIR_OP_B.webm
echo f | xcopy /y _voice_param.dat Compiled\_voice_param.dat
pause