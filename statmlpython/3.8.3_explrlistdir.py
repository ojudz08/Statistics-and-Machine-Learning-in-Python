import os

# Walk
WD = os.path.join(mytmpdir, "git", "pystatsml", "datasets")

for dirpath, dirnames, filenames in os.walk(WD):
    print(dirpath, dirnames, filenames)
    

# glob, basename and file extension
import glob

filenames = glob.glob(os.path.join(mytmpdir, "git", "pystatsml", "datasets", "*", "tissue-*.csv"))

## take basename then remove extension
basenames = [os.path.splitext(os.path.basename(f))[0] for f in filenames]
print(basenames)


# shutil - High-level file operations
import shutil

src = os.path.join(tmpdir, "foobar", "myfile.txt")
dst = os.path.join(tmpdir, "foobar", "plop", "myfile.txt")
print("copy %s to %s" % (src, dst))

shutil.copy(src, dst)

print("File %s exists?" % dst, os.path.exists(dst))

src = os.path.join(tmpdir, "foobar", "plop")
dst = os.path.join(tmpdir, "plop2")
print("copy tree %s under %s" % (src, dst))

try:
    shutil.copytree(src, dst)
    
    shutil.rmtree(dst)
    
    shutil.move(src, dst)
    
except (FileExistsError, FileNotFoundError) as e:
    pass