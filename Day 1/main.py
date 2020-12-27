def main():
    txt = open("../codes.txt")
    l = {}
    for list in txt:
        i = int(list)
        if i in l:
            y = 2020 - i
            l[y] = i
        else:
            print("{0} + {1} = 2020\n{2} * {3} = {4}".format(i, l[i], i, l[i], i*l[i]))
        return 0
        
if __name__ == "__main__":
    main()