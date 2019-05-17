# File I/O

# csv

import tempfile, os.path
tmpdir = tempfile.gettempdir()
csv_filename = os.path.join(tmpdir, "user.csv")
users.to_csv(csv_filename, index=False)
other = pd.read_csv(csv_filename)