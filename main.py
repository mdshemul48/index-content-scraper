from urllib.parse import urlparse


url_link = urlparse(
    "http://ftp1.circleftp.net/SERVER-1/DRIVE-1/ftp1/PC%2C%20Consoles%20Games%20%26%20Mods/PC%20Game%20Backup/A%20Way%20Out%20%28Steam%20Backup%20February%2025%2C%202021%29/"
)


print(url_link.netloc)
