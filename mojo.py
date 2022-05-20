# read input
def import_mojo():
    with open("./files/mojo.txt") as f:
        return [line.strip() for line in f.read().strip().split('\n')]

# main method
def main():
    search_term = "MOJO"
    mojo = import_mojo()

    valid = [search_term, search_term[::-1]]

    # case 1: a square
    if "".join(mojo) == search_term:
        for y in range(len(mojo)):
            for x in range(len(mojo[y])):
                print(f"{mojo[y][x]}: {x},{y}")

        return 

    # case 2: horizontal
    for y in range(len(mojo)):
        for x in range(len(mojo[y]) - len(search_term) + 1):
            row = mojo[y][x:x+len(search_term)]
            if row in valid:
                normal = row == search_term

                # print coords of each letter
                for i in (range(len(search_term)) if normal else range(len(search_term) - 1, -1, -1)):
                    print(f"{row[i]}: {x+i},{y}")
                
                return

    # case 3: vertical
    for x in range(len(mojo[0])):
        for y in range(len(mojo) - len(search_term) + 1):
            column = "".join([mojo[y+i][x] for i in range(len(search_term))])
            if column in valid:
                normal = column == search_term

                # print coords
                for i in (range(len(search_term)) if normal else range(len(search_term) - 1, -1, -1)):
                    print(f"{column[i]}: {x},{y+i}")
                
                return

main()