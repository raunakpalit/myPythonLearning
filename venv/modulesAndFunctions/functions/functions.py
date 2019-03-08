def python_food():
    width = 80
    text = ("Spam and eggs")
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)

with open("centred", "w") as centred_file:
    # Call the function
    centre_text("Spam and eggs", file=centred_file)
    centre_text("Spam, spam and eggs", file=centred_file)
    centre_text(12, file=centred_file)
    centre_text("Spam, spam, spam and spam", file=centred_file)

    centre_text("first", "second", 3, 4, "five", sep=':', file=centred_file)