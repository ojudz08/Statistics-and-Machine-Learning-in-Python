# For more advanced use cases, the underlying Popen interface can ce used directly
# Run the command described by args
# Wait for the command to complete
# return a CompletedProcess instance
# Does not capture stdout or stderr by default. To do so, pass PIPE for the stdout and/or stderr argument


import subprocess

# doesn't capture output
p = subprocess.run(["ls", "-l"])
print(p.returncode)

# Run through the shell
subprocess.run("ls -l", shell=True)

# Capture output
out = subprocess.run(["ls", "-a", "/"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# out.stdout is a sequence of bytes that should be decoded into a utf-8 string
print(out.stdout.decode('utf-8').split("\n")[:5])