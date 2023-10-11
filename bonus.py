# Bonus, create a new python file and do the following:

# Define a string variable containing a sentence with at least 10 words.
sentence = "Hi my name is Khamis and I love watching and playing football"
# Define a string variable containing a word that appears in the sentence.
appearedWord = "love"
# Print the length of the sentence.
print(len(sentence))
# Print the index of the first occurrence of the word in the sentence.
indexNum = sentence.find(appearedWord)
print(indexNum)
# Print the number of times the word appears in the sentence.
countNum = sentence.lower().count(appearedWord)
print(f"The word '{appearedWord}' appears {countNum} times in the sentence.")
# Print the sentence in all uppercase letters.
print(sentence.upper())
# Print the sentence in all lowercase letters.
print(sentence.lower())
# Replace the word in the sentence with a new word of your choice.
print(sentence.replace("Khamis", "Mansour"))
# Print the last character of the sentence.
print(sentence[-1])