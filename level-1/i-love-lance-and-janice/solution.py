def solution(text):
    import string
    alphabet = string.ascii_lowercase
    alphabet_reversed = alphabet[::-1]
    
    new_text = []
    words = text.split()

    for word in words:
        letters = list(word)
        for i in range(len(letters)):
            if letters[i] in alphabet:
                char_index = alphabet.index(letters[i])
                new_char = alphabet_reversed[char_index]
                letters[i] = new_char
        new_text.append(''.join(letters))
    return ' '.join(new_text)
    
test_cases = [
    "wrw blf hvv ozhg mrtsg'h vkrhlwv?",
    "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!",
]
for i in test_cases:
    print("\nEncrypted message: %s" % i)
    print("Decrypted message: %s" % solution(i))
