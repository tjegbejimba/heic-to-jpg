#HEIC to JPG image format batch conversion script for Python 3. Tested on Windows 10.
#You will need to have ImageMagick installed: https://www.imagemagick.org/

import os, subprocess, sys

files = sys.argv
print(files[1])
for f in files:
    if f.lower().endswith(".heic"): 
        print("hello3")
        print('Converting %s...' % f)
        subprocess.run(["magick", "%s" % f, "%s" % (f[0:-5] + '.jpg')])
        continue