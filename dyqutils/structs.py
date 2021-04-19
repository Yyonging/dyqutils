from t import ListNode, Node
from typing import Union
from pyecharts.charts import Page
from pyecharts.charts import Tree
from pyecharts import options as opts


def generate_nodes(n: Union[int,list]):
    '''generate tree by list or range(n)'''
    lns = [ListNode(i) for i in (n if isinstance(n, list) else range(n))]
    for i, node in enumerate(lns):
        try:
            node.next = lns[i+1]
        except:
            node.next = None
    lns[-1].next = None
    return lns[0]

def print_nodes(head:ListNode):
    while head:
        print(f'{head=}')
        head = head.next

def generate_tree(n:list):
    '''通过数组生成一颗二叉树'''
    nodes = [Node(i) for i in n]
    for i, _ in enumerate(nodes):
        if 2*i+1 < len(nodes):
            nodes[i].left = nodes[2*i+1]
        if 2*i+2 < len(nodes):
            nodes[i].right = nodes[2*i+2]
    return nodes[0]

def print_tree(root:Node):
    def traverse(root):
        t = {
            "name":"",
            "children":[]
        }
        # import pdb; pdb.set_trace()
        t['name'] = root.val
        if root.left:
            t["children"].append(traverse(root.left))
        if root.right:
            t['children'].append(traverse(root.right))
        return t
    res = traverse(root)
    from rich import print
    print(res)
    return res

def generate_echarts_data(root:Node):
    def traverse(root):
        t = {
            "name":"",
            "children":[]
        }
        t['name'] = root.val
        if root.left and root.left.val is not None:
            t["children"].append(traverse(root.left))
        if root.right and root.right.val is not None:
            t['children'].append(traverse(root.right))
        return t
    res = traverse(root)
    print(res)
    return [res]

def tree_render(roots=list[Node], fname='render.html'):
    def generate_bar():
        for root in roots:
            data = generate_echarts_data(root)
            c = Tree().add(
                    series_name="tree",
                    data=data,
                    orient="TB",
                    initial_tree_depth=20,
                    label_opts=opts.LabelOpts(),
                    leaves_label_opts=opts.LabelOpts(),
                )
            yield c
    Page(layout=Page.SimplePageLayout).add(*list(generate_bar())).render(fname)


if __name__ == "__main__":
    print_nodes(generate_nodes(6))
    print_nodes(generate_nodes([1,3,4,5,6,7]))
    print('---------------')
    root = generate_tree([1,2,3,4,5,6])
    print_tree(root)
    root = generate_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    tree_render([root])
