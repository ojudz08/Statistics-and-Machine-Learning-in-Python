import os

# Get the current working directory
cwd = os.getcwd()
print(cwd)

# Set the current working directory
os.chdir(cwd)


import tempfile

# Get temporary directory
tmpdir = tempfile.gettempdir()
print(tmpdir)


# Join paths
mytmpdir = os.path.join(tmpdir, "foobar")

# list containing the names of the entries in the directory given by the path
os.listdir(tmpdir)
print(mytmpdir)


# Create directory
if not os.path.exists(mytmpdir):
    os.mkdir(mytmpdir)
    
mytmpdir2 = os.makedirs(os.path.join(tmpdir, "foobar", "plop", "toto"), exist_ok=True)
print(mytmpdir2)