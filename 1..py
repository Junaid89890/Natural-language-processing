import re
def regex_example():
    text = "This is a test string ending with ab and another one ends with xyab"
    pattern = r".*ab$"

    match = re.search(pattern, text)
    
    if match:
        print(f"Match found: {match.group()}")
    else:
        print("No match found.")
    matches = re.findall(pattern, text)
    print("All matches in text:", matches)
regex_example()
