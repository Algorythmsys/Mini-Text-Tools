def caesar(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            offset = (ord(ch) - base + shift) % 26
            result.append(chr(base + offset))
        else:
            result.append(ch)
    return "".join(result)

if __name__ == "__main__":
    mode = input("encode/decode: ").strip().lower()
    text = input("Text: ")
    shift = int(input("Shift (1-25): "))
    if mode == "decode":
        shift = -shift
    print("Result:", caesar(text, shift))
