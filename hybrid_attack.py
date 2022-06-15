import itertools
import zlib
import time

import pyzipper


def main():
    words = []
    with open("homer_simpson_profile.txt", encoding="utf-8") as profile:
        rows = profile.readlines()
        for row in rows:
            row = row.strip()
            words.append(row.lower())
            if not row.isdigit():
                words.append(row.capitalize())

    start_time = time.time()
    with pyzipper.AESZipFile("homer_simpson.zip") as my_zip:
        for i in range(len(words) + 1):
            for combination in itertools.product(words, repeat=i):
                my_password = bytes("".join(combination), encoding="utf8")

                try:
                    print(my_password)
                    my_zip.extractall(pwd=my_password)
                except (RuntimeError, zlib.error) as error:
                    continue
                else:
                    current_timing = time.time() - start_time
                    current_timing = round(current_timing / 60, 4)

                    print("Time -> " + str(current_timing ) + "min")
                    print("Password -> " + str(my_password))
                    return


if __name__ == "__main__":
    main()
