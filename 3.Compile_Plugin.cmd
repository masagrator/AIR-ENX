cd Plugin
bash -c "export DEVKITPRO=/opt/devkitpro; export DEVKITARM=/opt/devkitpro/devkitARM; make"
cd ../
echo f | xcopy /y Plugin\subsdk9 atmosphere\contents\0100ADC014DA0000\exefs\subsdk9
echo f | xcopy /y Plugin\main.npdm atmosphere\contents\0100ADC014DA0000\exefs\main.npdm
cd Plugin
bash -c "export DEVKITPRO=/opt/devkitpro; export DEVKITARM=/opt/devkitpro/devkitARM; make clean"
pause