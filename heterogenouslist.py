def flatten(heterogenous):
    out = []
    def recursive(heterogenous):
        for item in heterogenous:
            if isinstance(item,(list, tuple)):
                print("run")
                recursive(item)
            else:
                out.append(item)
    recursive(heterogenous)
    return out




lelist = [1,2,"a","b",("c",3,"d"),["e","f","g",3.14],(["y",4],("z",5))]
lelist=flatten(lelist)
print(lelist)

