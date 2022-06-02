#!/usr/bin/python3
def unhid():
    import hidden_4
    objx = (dir(hidden_4))
    for n in objx:
        if (n[:2] != "__"):
            print(n)


if __name__ == "__main__":
    unhid()
