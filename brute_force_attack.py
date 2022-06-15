import pyzipper
from string import ascii_lowercase
from itertools import product

lower_alpha = ascii_lowercase

with pyzipper.AESZipFile("staryarchiv.zip") as my_zip:
    for comb in product(lower_alpha, repeat=3):
        my_password = bytes("".join(comb), encoding="utf8")

        try:
            my_zip.extractall(pwd=my_password)
        except RuntimeError as error:
            continue
        else:
            print(my_password)
            break