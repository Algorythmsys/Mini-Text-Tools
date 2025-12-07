def count_words(s: str) -> int:
  return len(s.split())
if __name__ == "__main__":
  text = input("Enter text: ")
  print("Word count:", count_words(text))
