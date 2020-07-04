import csv
from collections import defaultdict


def ctree():
    return defaultdict(ctree)


def build_leaf(name, leaf, level):
    
    res = {}
    res["info"] = {}
    if (name != ""):
        res["info"] = {"name": name}
        
        # after level 1, use the next column as description
        if (level>1):
            res["info"]["description"] = list(leaf.keys())[0]
        # if there are items other than decription
        if len(leaf.keys()) > 1:
            lis = {}
            if (level>1):
                # after first row, skip the first child (as that would be description) and look in the items of second child (as second child would have empty name)
                lis = [build_leaf(k, v, level+1) for k, v in leaf[list(leaf.keys())[1]].items()]
                if len(lis) != 0:
                    res["items"] = lis
            else:
                # for first row, there's no description
                lis = [build_leaf(k, v, level+1) for k, v in leaf.items()]
                if len(lis) != 0:
                    res["items"] = lis
    return res
def main():
   
    tree = ctree()
   
    with open('final1.csv') as csvfile:
        reader = csv.reader(csvfile)

        # loop over all rows of data
        for rid, row in enumerate(reader):

            # skip first row
            if rid == 0:
                continue

            leaf = tree[row[0]]

            # loop over all elements in a row
            for cid in range(1, len(row)):
                leaf = leaf[row[cid]]
 
    res = []
    # build res
    for name, leaf in tree.items():
        res.append(build_leaf(name, leaf, 1))

   
    import json
    # give output
    print(json.dumps(res, sort_keys=False, indent=4))



main()