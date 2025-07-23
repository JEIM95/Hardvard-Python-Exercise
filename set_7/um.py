import re
def main():
    text = input("Text: ")
    print(count(text.lower()))

def count(s):
    result = 0

    if len(s) < 3:
        pattern = r'um'
    else:
        pattern = r'\bum\b' 

    list = re.findall(pattern, s)
    result = len(list)

    return result
 

if __name__ == "__main__":
    main()