def python_food():
    width = 80
    text = ("Spam and eggs")
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# Call the function
centre_text("Spam and eggs")
centre_text("Spam, spam and eggs")
centre_text(12)
centre_text("Spam, spam, spam and spam")

centre_text("first", "second", 3, 4, "five")