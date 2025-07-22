import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'src="https?://(?:www)?\.?youtube\.com/embed/([\w!\?\-=\+]+)" ?(.*)?'

    match = re.search(pattern, s)

    if match:
        final_url = match.group(1)
        url = f"https://youtu.be/{final_url}"
    else:
        url = "None"

    return url


if __name__ == "__main__":
    main()