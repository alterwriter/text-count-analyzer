def many_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
        
    return count

text = input("enter a string = ").lower()

for char in ("abcdefghijklmnopqrstuvwxyz"):
    counting = count_char(text,char)
    print(f"{char} = {counting} Value")
