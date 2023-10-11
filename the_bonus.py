sentence = "The weather is lovely today and I had a cup of coffee in the morning"
word = "morning"
print("the length of the sentence:" ,len(sentence))
print(f"location of {word} in the sentence is in:", sentence.find(word) )
print(f"{word} appeard in the sentence {sentence.count(word)} times")
print(f"the sentence in all uppercase letters: {sentence.upper()}")
print(f"the sentence in all lowercase letters: {sentence.lower()}")

new_word = sentence.replace(word,"Evening!")
print(new_word)

print(f"the last character of the sentence:{sentence[-1]}")