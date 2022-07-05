# GE-Downloader
Author: Sam Walters

Tired of going through the process of downloading the latest GE-proton tarballs, and extracting them to .steam/root/compatibilitytools.d/? I am too! Good thing we are programmers, and can spend hours automating minute tasks!

I've written a simple shell script and python script to make the whole process one command.

## The Python Script

This script takes an argument, "name" or "url", and spits out the latest GE-proton tarball url for the latter option, or the latest release's name for the former option.

the requirements are just click and requests, and can be found in `requirements.txt`

## The Shell Script

This script utilizes the python script to get both the latest package name and download url. It then extracts it to `.steam/root/compatibilitytools.d/` and removes the tarball afterwards. That is all!

## To Use:

1. Run the shell script

And thats it! You can even add an alias to `.bashrc` to bind running this to 'ge-update' or something so you can call it from anywhere.

So now you can save those precious minutes and instead spend them automating more stuff!