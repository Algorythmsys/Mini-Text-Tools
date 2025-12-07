def reverse_text(s: str) -> str:
  return s[::-1]
if __name__=="__main__"":
  text = input("Text to reverse: ")
  print(reverse_text(text))
