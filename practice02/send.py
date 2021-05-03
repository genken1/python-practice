def f21(arr):
    tree = {
        "asn.1": 11,
        "fancy": {
            "hcl": {
                "ebnf": {
                    1984: 0,
                    1967: 1
                },
                "plsql": 2,
                "r": 3
            },
            "gap": {
                1984: {
                    "ebnf": 4,
                    "plsql": 5,
                    "r": 6
                },
                1967: 7
            },
            "coq": {
                1977: 10,
                1999: {
                    1984: 8,
                    1967: 9
                }
            }
        }
    }
    f_node = tree.get(arr[1])
    if type(f_node) is not dict:
        return f_node
    s_node = f_node.get(arr[2])
    if arr[2] == "hcl":
        t_node = s_node.get(arr[0])
        if type(t_node) is dict:
            return t_node.get(arr[3])
        return t_node
    if arr[2] == "gap":
        t_node = s_node.get(arr[3])
        if type(t_node) is dict:
            return t_node.get(arr[0])
        return t_node
    if arr[2] == "coq":
        t_node = s_node.get(arr[4])
        if type(t_node) is dict:
            return t_node.get(arr[3])
        return t_node
