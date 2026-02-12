def find_lines_containing(filename, keyword):
    """
    Returns a list of (line_number, line_text) for lines that contain ←↩
        keyword
    (case-insensitive). Line numbers start at 1.
    """

    matching_lines = []
    keyword = keyword.lower()

    file = open(filename, "r")

    for line_number, line_text in enumerate(file):
        if keyword in line_text.lower():
            matching_lines.append((line_number, line_text))

    return matching_lines

filename = "sample-file.txt"
keyword = "lorem"
matching_lines = find_lines_containing(filename, keyword)

print("Number of matching lines: ", len(matching_lines))

for i, (line_number, line_text) in enumerate(matching_lines):
    print(f"{i+1}. Line {line_number}: {line_text}")