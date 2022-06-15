import pyzipper
import zlib

with pyzipper.AESZipFile("downloaded.zip") as my_zip:
    with open("rockyou.txt", encoding="utf-8") as rockyou:
        rows = rockyou.readlines()
        for row in rows:
            row = row.strip()
            my_password = bytes(row, encoding="utf8")

            try:
                my_zip.extractall(pwd=my_password)
            except (RuntimeError, zlib.error) as error:
                continue
            else:
                print(my_password)
                break
