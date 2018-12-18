import nameandmain1

print("top level in nameandmain2.py")
nameandmain1.func()


if __name__ == '__main__':
    print('2.py is being run directly')
else:
    print('2.py is being imported to anthor module')
    