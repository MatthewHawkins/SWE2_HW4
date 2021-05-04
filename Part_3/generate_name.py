
def create_name(first, last):
    if first.isalpha() and last.isalpha():
        return(first + " " + last)
    else:
        return "ERROR"