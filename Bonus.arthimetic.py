
advice = "if you can imagine it, you can achieve it. Have faith to achieve what you want"
word = "achieve"

print("the lenth of the advice is: ", len(advice))
print(f"location of {word} in the advice is in ", advice.find(word))
print(f"{word} appeard in the advice {advice.count(word)} times")
Print (f"the index of the first occurrence of the {word} in the advice is{advice.find(word)}")
print (advice.upper())
print (advice.lower())

new_advice = advice.replace(word, "get")
print(new_advice)

print (s"the last character of the advice is {advice[-1]}")
