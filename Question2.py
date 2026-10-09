sentence = input("Enter a sentence: ")

vowels = 0
spaces = 0
digits = 0

for ch in sentence:
    if ch.lower() in "aeiou":
        vowels += 1
    if ch == " ":
        spaces += 1
    if ch.isdigit():
        digits += 1

print("Number of characters:", len(sentence))
print("Number of words:", len(sentence.split()))
print("Number of vowels:", vowels)
print("Number of spaces:", spaces)
print("Number of digits:", digits)
