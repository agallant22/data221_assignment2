from string import punctuation

file = open(file = "sample-file.txt", mode = "r")

content = file.read()
# print(content)

tokens = content.split()
cleaned_tokens = []

for token in tokens:
    token = token.lower()
    token = token.strip(punctuation)       # remove punctuation somehow

    count = 0

    for letter in token:
        if letter.isalpha():
            count += 1

    if count >= 2:
        cleaned_tokens.append(token)

# print(cleaned_tokens)     # testing cleaning tokens

word_counts= {}

for word in cleaned_tokens:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words[:10]:
    print(f"{word}: {count}")

file.close()