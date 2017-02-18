import os
from os import path
import datetime
from datetime import date, time, timedelta
import time
import shutil
from zipfile import ZipFile

def main():
    print(os.name)

    print(str(path.exists("textfile.txt")))
    print(str(path.isfile("textfile.txt")))
    print(str(path.isdir("textfile.txt")))

    print(str(path.realpath("textfile.txt")))
    print(str(path.split(path.realpath("textfile.txt"))))

    # Get the modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("textfile.txt was modified ", str(td), " ago.")

    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")
        dir, file = path.split(src)
        print(dir,file)

        # Make a backup copy with the filename appended by "backup"
        dst = src + ".backup"
        shutil.copy(src, dst)
        # Copy over the permissions, modification times, etc
        shutil.copystat(src, dst)
        # Rename the backup to .bak
        os.rename("textfile.txt.backup", "textfile.txt.bak")
        # Put things into a zip archive
        shutil.make_archive("archive", "zip", dir)

        with ZipFile("textfiles.zip", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")

if __name__ == "__main__":
    main()

