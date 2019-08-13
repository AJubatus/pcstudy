'''
Count total lines of C code exluding comments below the current working directory

c comment starts with /*
ends with */
can be multiline

can be // also
'''
import glob


def parse():
    files = glob.glob("**/*.c", recursive=True)
    counter = 0

    for sourcefile in files:
        print(sourcefile)
        multiline = 0
        for line in open(sourcefile, encoding='UTF-8'):
            if multiline:
                if line.startswith('*/'):
                    multiline = False
                    # this assumes multiline won't have nested comments
                pass
            elif line.isspace():
                pass
            elif line.startswith('//'):
                pass
            elif line.startswith('/*'):
                if not line.endswith('*/'):
                    multiline == True
                pass
            else:
                counter += 1
    return counter


if __name__ == "__main__":
    print(parse())

