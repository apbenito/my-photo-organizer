#MY PHOTO ORGANIZER
##What is it?
This is a simple script that helps me work with the photos extracted from my camera. Right now is very specific for my purposes, as I only allow for the filenames that my camera automatically create (_MG_imgnumber), so it won't work for all cases. However, it is very easy to change for your own case

I also plan to add a possibility to specify a default file name so this script can be used more generally.
In the future (maybe) i will do some GUI design to make this script more user friendly

##How it works

1. Give it a folder full of photos (in my case i usually have somewhere from 100 to a 1000 photos per session). It can have multiple file extensions (.cr2 and .jpg in my case)
2. Look through your photos and select the ones that you can't use (blurry, closed eyes, etc) and write their name in a .txt file. Note: if you want to delete a bunch of consecutive pictures (e.g pictures 10,11,12,...,25) just write the first and last one separated by a dash (e.g. 10-25) and the program does it for you
3. Input the .txt file into the program and let it do its thing

##Future additions
- Possibility to create the folder containing all photos instead of inputting it
- Filter the selection photos in a similar way as deleting the bad ones (through .txt list)
- Add GUI to interact with all elements, with the option of having an image viewer
- Generalize for any naming convention (so it can be used in any case, not only for my camera lol)