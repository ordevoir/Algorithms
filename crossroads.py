
vertices = dict()
vertices['AB'] = ('BC','BD','DA','EA')
vertices['AC'] = ('BD','DA','DB','EA','EB')
vertices['AD'] = ('EA','EB','EC')
vertices['BA'] = ()
vertices['BC'] = ('AB','DB','EB')
vertices['BD'] = ('AB','AC','DA','EB','EC')
vertices['DA'] = ('AB','AC','BD','EB','EC')
vertices['DB'] = ('AC','BC','EC')
vertices['DC'] = ()
vertices['EA'] = ('AB','AC','AD')
vertices['EB'] = ('AC','AD','BC','BD','DA')
vertices['EC'] = ('AD','BD','DA','DB')
vertices['ED'] = ()

remainVerts = set(vertices.keys())

def greedy(vertices, remainVerts):

    color = 0
    dictionary = dict()
    while len(remainVerts) > 0:
        st = {remainVerts.pop()}
        # print(st, color)
        # remainVerts = remainVerts.difference(st)
        for key in remainVerts:
            found = False
            for i in st:
                if key in vertices[i]:
                    found = True
                    break
            if found == False:
                st.add(key)
        remainVerts = remainVerts.difference(st)
        dictionary[color] = st
        color += 1
    return dictionary

dictionary = greedy(vertices, remainVerts)

for key in dictionary:
    print(key, dictionary[key])
