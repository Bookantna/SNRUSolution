from cs50 import get_string

text = "One fish. Two fish. Red fish. Blue fish."

while True:
    countwords = 1
    countsentences = 0
    countletters = 0
    for i in range(len(text)):
        if text[i] == ' ':
            countwords +=1
        if text[i] == '!' or text[i] == '?' or text[i] == '.':
            countsentences +=1
        if (text[i] >= 'a' and text[i] <= 'z') or (text[i] >= 'A' and text[i] <= 'Z'):
            countletters +=1
    print(countwords)
    print(countsentences)
    print(countletters)
    index = round(0.0588 * (100 * float (countletters / countwords)) - 0.296 * (100 * float(countsentences / countwords)) - 15.8)
    if index >= 16:
        print("Grade 16")
    elif index <= 1:
        print("Before Grade 1")
    else:
        print("Grade ",index)
    
    break

