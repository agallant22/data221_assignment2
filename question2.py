from string import punctuation

file = open(file = "sample-file.txt", mode = "r")

content = file.read()

tokens = content.split()
cleaned_tokens = []

# Clean tokens
for token in tokens:
    token = token.lower()
    token = token.strip(punctuation)

    count = 0

    for letter in token:
        if letter.isalpha():
            count += 1

    if count >= 2:
        cleaned_tokens.append(token)

bigram_count = {}

for i in range(len(cleaned_tokens) - 1):
    bigram = cleaned_tokens[i] + " " + cleaned_tokens[i + 1]
    bigram_count[bigram] = bigram_count.get(bigram, 0) + 1

sorted_bigram = []

for bigram in bigram_count:
    sorted_bigram.append((bigram, bigram_count[bigram]))

for i in range(len(sorted_bigram)):
    for j in range(i + 1, len(sorted_bigram)):
        if sorted_bigram[j][1] > sorted_bigram[i][1]:
            sorted_bigram[i], sorted_bigram[j] = sorted_bigram[j], sorted_bigram[i]

for bigram, count in sorted_bigram[:5]:
    print(f"{bigram} -> {count}")