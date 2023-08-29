def plain_format():
    text = input("Text: ")
    return text


def bold_format():
    text = input("Text: ")
    to_return = f"**{text}**"
    return to_return


def italic_format():
    text = input("Text: ")
    to_return = f"*{text}*"
    return to_return


def header_format():
    while True:
        level = int(input("Level: "))
        if 0 < level <= 6:
            break
        else:
            print("The level should be within the range of 1 to 6")

    text = input("Text: ")

    try:
        if to_print[-1] != "\n":
            to_return = f"\n{r'#' * level} {text}\n"
        else:
            to_return = f"{r'#' * level} {text}\n"
        return to_return
    except IndexError:
        to_return = f"{r'#' * level} {text}\n"

    return to_return

def link():
    label = input("Label: ")
    url = input("URL: ")
    to_return = f"[{label}]({url})"
    return to_return


def inline_format():
    text = input("Text: ")
    to_return = f"`{text}`"
    return to_return


def new_line():
    return "\n"


formatters = {"plain": plain_format,
              "bold": bold_format,
              "italic": italic_format,
              "header": header_format,
              "link": link,
              "inline-code": inline_format,
              "new-line": new_line}


done = False
to_print = []

while not done:

    select_format = input("Choose a formatter: ")

    if select_format == "!help":
        print("Available formatters: plain bold italic header link inline-code new-line")
        print("Special commands: !help !done")
        continue

    elif select_format == "!done":
        exit()

    if select_format in formatters.keys():
        to_print.append(formatters[select_format]())
        print("".join(to_print))

    else:
        print("Unknown formatting type or command")
        continue
