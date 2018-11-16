#!/bin/sh

if [[ $(whoami) != "root" ]]; then
    echo "Error: script not running as root or with sudo! Exiting..."
    exit 1
fi

for zip in *.zip
do
  dirname=`echo $zip | sed 's/\.zip$//'`
  if mkdir "$dirname"
  then
    if cd "$dirname"
    then
      unzip ../"$zip"
      echo "File $zip unziped."
      cd ..
      rm -f $zip # Uncomment to delete the original zip file
      echo "File $zip deleted. Unziped dir remains."
    else
      echo "Could not unpack $zip - cd failed"
    fi
  else
    echo "Could not unpack $zip - mkdir failed"
  fi
done

echo "Updating to latest version..."
maldet -d

echo "Updating virus signatures..."
maldet -u

echo "Starting maldet scan..."

maldet -a "$PWD"
