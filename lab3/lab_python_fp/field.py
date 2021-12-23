def field(data, *args):
    if len(args) == 1:
        for i in data:
            if args[0] in i:
                yield i[args[0]]
    else:
        for i in data:
            tmp = dict()
            for j in args:
                if j in i:
                    tmp[j] = i[j]
            yield tmp