
def rec_sum(root, depth):
    ans = depth
    for el in root.values():
        ans += rec_sum(el, depth + 1)
    return ans


def find_path(root, target):
    for lab, sub in root.items():
        if lab == target:
            return [lab]
        res = find_path(sub, target)
        if res:
            return [lab, *res]
    return None


def task1(tree):
    print(rec_sum(tree, 0))

def task2(tree):
    pa = find_path(tree, 'SAN')
    pb = find_path(tree, 'YOU')

    lca_depth = 0
    for ea, eb in zip(pa, pb):
        if ea != eb:
            break
        lca_depth += 1

    print(len(pa) + len(pb) - lca_depth * 2 - 2)



if __name__ == '__main__':
    tree = {}
    while 1:
        try:
            par, sub = input().strip().split(')')
        except EOFError:
            break

        if par not in tree:
            tree[par] = {}
        if sub not in tree:
            tree[sub] = {}
        tree[par][sub] = tree[sub]

    # task1(tree['COM'])
    task2(tree['COM'])
