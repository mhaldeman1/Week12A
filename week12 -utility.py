def PrintOutput(a):
    Print = 'OUTPUT ' + a
    print(Print)
def LoadFile(a):
    read = open(a, 'r')
    x = []
    for i in read:
        x.append(i)
    PrintOutput(x)
def UpdateString(a,b,c):
    x = ln a.count(b)
def FindWordCount(a,b):
    return a.count(b)
def ScoreFinder(a,b,c):
    d = []
    for i in a:
       d.append(i.lower())
    try:
        x = d.index(c.lower())
        PrintOutput(c, 'got a score of ' + str(b[x]))
    except:
        print('OUTPUT player not found')
def Union(a,b):
    List = []
    for i in b:
        a.append(i)
    for i in a:
        List.append(str(i))
    for i in List:
        if List.count(i) > 1:
            c = ''.join(List)
            d = c.rindex(i)
            List = List[:d - 1] + List[d:]
    return List
def Intersection(a,b):
    c = []
    for i in a:
        if i in b:
            c.append(i)
    return c
def NotIn(a,b):
    c = []
    for i in a:
        if i not in b:
            c.append(i)
    return c

