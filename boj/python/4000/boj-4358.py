import sys

tree_dict = {}
lines = sys.stdin.read()
trees = list(filter(lambda x: x != "", lines.split('\n')))
        
for name in trees:
    if name == "": continue
    if name in tree_dict: tree_dict[name] += 1
    else: tree_dict[name] = 1

total = sum(tree_dict.values())

for key in sorted(tree_dict.keys()):
    print("%s %.4f"%(key, tree_dict[key]/total * 100))