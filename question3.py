from string import punctuation

file = open(file = "sample-file.txt", mode = "r")

content = file.readlines()

groups = {}

for i, line in enumerate(content, start=1):
    normalized = line.lower()
    normalized = normalized.rstrip()
    normalized = "".join(normalized.split())

    for j in punctuation:
        normalized = normalized.replace(j, "")

    if normalized == "":
        continue

    if normalized not in groups:
        groups[normalized] = []

    groups[normalized].append((i, line.rstrip()))

near_duplicates = [group for group in groups.values() if len(group) > 1]

print("Number of near duplicates: ", len(near_duplicates))
print()

for k, group in enumerate(near_duplicates[:2], start=1):
    print(f"Set {k}:")
    for line_num, text in group:
        print(f" Line {line_num}: {text}")
    print()