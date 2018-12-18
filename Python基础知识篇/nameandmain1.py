def func():
    print("func() in nameandmain1.py")


print("top_level in 1 py")

if __name__ == '__main__':
    print("1.py is being run directly")
else:
    print("1.py is being imported into another module")
