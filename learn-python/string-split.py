speech = "variable, of, things"
x = speech.split(",")
print ("split text is:", x)


text = "Somespacesaround"
stripped_text = text.strip()
print("Stripped text:", stripped_text)


str = '          1111Hello1111          '
print(str.strip('              '))

text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")