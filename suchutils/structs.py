from .t import ListNode, Node
from typing import Union, Generator
from pyecharts.charts import Page, Tree, Graph
from pyecharts import options as opts
from rich import print

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
    print(list(linked_to_list(head)))

def linked_to_list(node:ListNode):
    while node:
        yield node
        node = node.next

def nodes_render(nodes:list[list[Node]], fname='render_nodes.html'):
    def generate_graph():
        for line in nodes:
            last_node = None
            for node in line[::-1]:
                t = {
                    "name":"",
                    "children":[]
                }
                t['name'] = str(node.val)
                if last_node:
                    t['children'].append(last_node)
                last_node = t
            c = Tree().add(
                    series_name="tree",
                    data=[last_node],
                    orient="LR",
                    initial_tree_depth=20,
                    label_opts=opts.LabelOpts(),
                    leaves_label_opts=opts.LabelOpts(),
                )
            yield c
    Page(layout=Page.SimplePageLayout).add(*list(generate_graph())).render(fname)

def generate_tree(n:list):
    '''通过数组生成一颗二叉树'''
    nodes = [Node(i) for i in n]
    for i, _ in enumerate(nodes):
        if 2*i+1 < len(nodes) and (nodes[2*i+1].val is not None):
            nodes[i].left = nodes[2*i+1]
        if 2*i+2 < len(nodes) and (nodes[2*i+2].val is not None):
            nodes[i].right = nodes[2*i+2]
    return nodes[0]

def print_tree(root:Node):
    def traverse(root):
        t = {
            "name":"",
            "children":[]
        }
        t['name'] = root.val
        if root.left:
            t["children"].append(traverse(root.left))
        if root.right:
            t['children'].append(traverse(root.right))
        return t
    res = traverse(root)
    print(res)
    return res

def generate_echarts_data(root:Node):
    def traverse(root):
        t = {
            "name":"",
            "children":[]
        }
        t['name'] = str(root.val)
        if root.left:
            t["children"].append(traverse(root.left))
        if root.right:
            t['children'].append(traverse(root.right))
        return t
    res = traverse(root)
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
    print_nodes(generate_nodes([1,2,3]))
    nodes = [[ListNode(i) for i in range(5)], list(linked_to_list(generate_nodes(8)))]
    nodes_render(nodes)
    print('---------------')
    root = generate_tree([1,2,3,4,5,6])
    print_tree(root)
    root = generate_tree([1,2,3,4,5,6,7,8,9,10,11,None,13,14,15])
    print_tree(root)
    tree_render([root])
