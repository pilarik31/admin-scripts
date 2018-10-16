#!/bin/bash

input="wgetlist.txt"
outputDir="./autowgetOutput/"

echo "===KONTROLA==="
echo "Spuštěno z: $PWD"
echo "Vstup: $input"
echo "Výstupní složka: $outputDir"
if [ ! -f $input ] 
then
    echo "Vstupní soubor ($input) neexistuje! Ukončuji..."
    exit
else
    echo "Vstupní soubor existuje."
fi

if [ ! -d $outputDir ] 
then
    echo "Výstupní složka neexistuje, vytvářím $outputDir"
    mkdir  $outputDir
else
    echo "Výstupní složka existuje."
fi
echo "===KONEC KONTROLY==="
echo "===ZAČÁTEK STAHOVÁNÍ==="


while IFS= read LINE 
do
    wget $LINE -P $outputDir
done <"$input"



