def convert (text):
   smile = "🙂"
   sad = "🙁"
   m_text = text.replace(":)",smile).replace(":(",sad)
   return m_text

def main():
   text = input("Write someting with emoticons. This :) or this:(: ")
   emoji_text = convert(text)
   print(emoji_text)


main()