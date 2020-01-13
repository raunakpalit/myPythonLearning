def center_text(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)

# call the function
center_text("spam and eggs")
center_text("spam, spam and eggs")
center_text(12)
center_text("spam, spam, spam and spam")

center_text("first", "second", 3, 4, "spam")
