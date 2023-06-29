val = 1

def test():
    global val
    val = 2
    print("value = ",val)


if __name__ == "__main__":
    test()
    print(val)