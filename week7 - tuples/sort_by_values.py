c = {'a' : 10, 'b' : 1, 'c' : 22}
tmp = list()
for k,v in c.items():
    tmp.append( (v, k))
    
print (tmp)

tmp.sort(reverse = False)
print (tmp)