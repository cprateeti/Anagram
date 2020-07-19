import enchant
f=enchant.Dict("en_US")
def substring(s,n):
    t=[]
    for p in range(n):
        for len in range(p+1,n+1):
            t.append(s[p:len])
    return t
def permutations(elements):
    if len(elements) <=1:
        return elements
    else:
        tmp=[]
        for perm in permutations(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0:1] + perm[i:])
        return tmp
list=[]
list1=[]
list2=[]
list=permutations("funeral")
for j in list:
    if(f.check(j)):
        print(j)
list1 = substring("funeral",len("funeral"))
for q in list1:
    if(len(q)>1 and q!="funeral"):
        list2=permutations(q)
        for r in list2:
            if(f.check(r)):
                print(r)
