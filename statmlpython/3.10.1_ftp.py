# Full FTP features with ftplib
import ftplib
ftp = ftplib.FTP("ftp.cea.fr")
ftp.login()

ftp.cwd('path')     # Intended to be empty
ftp.retrlines('LIST')

fd = open(os.path.join(tmpdir, "readme1.rst"), "wb")
ftp.retrbinary('RETR readme.rst', fd.write)
fd.close()
ftp.quit()

# File download urllib
import urlib.request
ftp_url = 'path/readme.rst'     # Intended to be impty
urllib.request.urlretrieve(ftp_url, os.path.join(tmpdir, "readme2.rst"))