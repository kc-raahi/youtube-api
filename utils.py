from unidecode import unidecode


def fix_title(title, chars):
    if len(chars) == 0:
        return unidecode(title)
    elif len(chars) == 1:
        return unidecode(title.replace(chars[0], ''))
    else:
        return unidecode(fix_title(title, chars[1:]).replace(chars[0], ''))
