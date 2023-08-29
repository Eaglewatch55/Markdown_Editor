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


def listed(ordered: bool):
    def row_formatting(rows, order):
        formatted = []
        if order:
            for j, row in enumerate(rows):
                formatted.append(f"{j + 1}. {row}")
        else:
            for row in rows:
                formatted.append(f"* {row}")

        return "\n".join(formatted) + "\n"

    while True:
        n = int(input("Number of rows: "))
        if n < 1:
            print("The number of rows should be greater than zero")
            continue
        else:
            break

    r = []

    for i in range(n):
        r.append(input(f"Row #{i + 1}: "))

    return row_formatting(r, ordered)


def new_line():
    return "\n"


formatters = {"plain": plain_format,
              "bold": bold_format,
              "italic": italic_format,
              "header": header_format,
              "link": link,
              "inline-code": inline_format,
              "ordered-list": (listed, True),
              "unordered-list": (listed, False),
              "new-line": new_line}


done = False
to_print = []

while not done:

    select_format = input("Choose a formatter: ")

    if select_format == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
        continue

    elif select_format == "!done":
        f = open("output.md", "w")
        f.write("".join(to_print))
        f.close()
        exit()

    if select_format in formatters.keys():
        try:
            to_print.append(formatters[select_format]())
        except TypeError:
            to_print.append(formatters[select_format][0](formatters[select_format][1]))

        print("".join(to_print))

    else:
        print("Unknown formatting type or command")
        continue
