#Define a string variable containing a sentence with at least 10 words.
sentence = "I think we are going to have a good day"
#Define a string variable containing a word that appears in the sentence.
word_from_sentence = "good"
#Print the length of the sentence.
print(f"length of the sentence: {len(sentence)}")
#Print the index of the first occurrence of the word in the sentence.
print(f"the first occurrence of the word in the sentence: {sentence.find(word_from_sentence)}")
#Print the number of times the word appears in the sentence.
print(f"the number of times the word appears in the sentence: {sentence.count(word_from_sentence)} " + "times")
# Print the sentence in all uppercase letters.
print("the sentence in all uppercase letters: "+ sentence.upper())
#Print the sentence in all lowercase letters.
print("the sentence in all lowercase letters: " +sentence.lower())
#Replace the word in the sentence with a new word of your choice
print(f"Reblasce th word (good) with the word (bad): {sentence.replace( word_from_sentence , "bad")}")
#Print the last character of the sentence.
print("the last character of the sentence: "+ sentence[-1])