def no_dups(s):
    # Your code here
    words = s.split()
    used = set()
    output = ''

    for word in words:
        if word not in used:
            used.add(word)
            if output != '':
                output += ' '
            output += word

    return output



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))