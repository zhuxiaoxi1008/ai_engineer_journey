def readText():
    f = open('./readme.md', 'r', encoding='utf-8')
    print(f.read())
    f.close()

def writeText():
    with open('./readme.md', 'a') as f:
        f.write('This is a IO WRITE TEST hello world io!\n')

if __name__ == '__main__':
    writeText()
    readText()

