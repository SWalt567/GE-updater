#!/bin/bash

# this script gets the download link to the current GE proton
# version and extracts the tarball to .steam/root/compatibilitytools.d/.
# it also removes the tarball after extraction for cleanup

usage() {
		echo
		echo "Usage: ge_update.sh [option...]"
		echo
		echo "This script gets downloads the latest GE-proton tarball and"
        echo "extracts it in the .steam/root/compatibilitytools.d/ dir"
		echo
		echo "          -h, --help              display this message"
		echo
}

set -e

while [ "$1" != "" ]; do 
    case $1 in
    -h | --help)
        usage
        exit
        ;;
    *)
        usage
        exit 1
        ;;
    esac
    shift
done

echo "grabbing url"

# grab the tarball url
tar_url=$(python ge_query.py url)
# grab the tarball name
tar_name=$(python ge_query.py name)

echo "navigating to .steam/root/compatibilitytools.d/"
cd /home/$USER/.steam/root/compatibilitytools.d/

echo $tar_url
echo $tar_name

wget $tar_url

echo "extracting tarball"
tar -xf $tar_name -C /home/$USER/.steam/root/compatibilitytools.d/

echo "removing tarball"
rm $tar_name