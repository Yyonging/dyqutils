dyqutils
-----
some useful code snippets.
my super utils in daily coding life.

Installing
-----

Install and update using `pip`:



    pip install -U dyqutils


A Simple Example
-----

.. code-block:: python

    from dyqutils.structs import *

    print_nodes(generate_nodes(6))
    print_nodes(generate_nodes([1,3,4,5,6,7]))
    print('---------------')
    root = generate_tree([1,2,3,4,5,6])
    print_tree(root)
    root = generate_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    tree_render([root])
