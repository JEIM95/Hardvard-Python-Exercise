import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^([0-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).([0-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).([0-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).([0-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
    matches = re.search(pattern, ip)

    if matches:
        result = "True"
    else:
        result = "False"
        
    return result


if __name__ == "__main__":
    main()