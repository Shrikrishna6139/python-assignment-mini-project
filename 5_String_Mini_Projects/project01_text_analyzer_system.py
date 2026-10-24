# Mini Project 1: Text Analyzer System
import string


def analyze_text(text):
  
    # --- basic counts ---
    chars = len(text)
    words = text.split()
    # a sentence ends with ., ! or ?
    sentences = text.count(".") + text.count("!") + text.count("?")

    vowels = consonants = digits = special = 0
    for ch in text:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1
        elif ch.isdigit():
            digits += 1
        elif ch != " " and ch not in "\n\t":
            special += 1

    print("\n========== TEXT ANALYSIS REPORT ==========")
    print("Total characters :", chars)
    print("Total words      :", len(words))
    print("Total sentences  :", sentences)
    print("Vowels           :", vowels)
    print("Consonants       :", consonants)
    print("Digits           :", digits)
    print("Special chars    :", special)
    print("Uppercase text   :", text.upper())
    print("Lowercase text   :", text.lower())

  
    print("Without extra spaces:", " ".join(words))


    freq = {}
    for w in words:
        w = w.lower().strip(string.punctuation)
        if w == "":
            continue
        freq[w] = freq.get(w, 0) + 1

    print("\nWord frequency:")
    for w, c in freq.items():
        print("  ", w, "->", c)
    return freq


def main():
    text = input("Enter a sentence or paragraph:\n")
    if text.strip() == "":
        print("You did not enter any text.")
        return

    freq = analyze_text(text)

    target = input("\nEnter a word to search for: ").lower().strip()
    if target in freq:
        print("'" + target + "' is present", freq[target], "time(s)")
    else:
        print("'" + target + "' is not present in the text")


main()
