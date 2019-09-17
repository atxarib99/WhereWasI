#!/bin/sh

#  Installer.sh
#
#  This installer will ask the user for an installation directory. It will assume a default installation directory of usr/local/wherewasi/Main.py.
#
#  Created by Arib Dhuka on 9/17/19.
#  

echo "Welcome to the WhereWasI installer!"

echo "For default options press enter"

echo "Define installation directory [/usr/local/wherewasi]:"

read installationdir

if [ -z "$installationdir" ]
then
    actualdir="/usr/local/wherewasi"
else
    actualdir=$installationdir
fi

if [ ! -d "$actualdir" ]
then
    mkdir "$actualdir"
    mkdir "$actualdir/files"
fi

if [ -e "$actualdir/File.py" ]
then
    rm "$actualdir/File.py"
fi
if [ -e "$actualdir/Main.py" ]
then
    rm "$actualdir/Main.py"
fi
if [ -e "$actualdir/Project.py" ]
then
    rm "$actualdir/Project.py"
fi
cp File.py "$actualdir/File.py"
cp Main.py "$actualdir/Main.py"
cp Project.py "$actualdir/Project.py"

FILENAME="wherewasi"
if [ -e $FILENAME ]
then
    rm $FILENAME
fi

echo "#!/bin/bash" > $FILENAME
echo "python $actualdir/Main.py $actualdir/files/ \$@" > $FILENAME
mv $FILENAME "/usr/local/bin/$FILENAME"
chmod +x "/usr/local/bin/$FILENAME"
