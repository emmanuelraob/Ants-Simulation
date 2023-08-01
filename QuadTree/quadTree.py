from QuadTree.node import Node
import math

class QuadTree: 
    #depth: max depth of the tree
    #x,y: left superior edge 
    #width, height: area covered bi the tree in pixels 
    #objects: list of objets 
    def __init__(self, depth, x, y, width, height, objects):
        self.root = Node(x, y, width, height, objects, 0)
        self.build(self.root, depth, 0)
        self.depth = depth

    def build(self, node, depth, level):
        if node.level >= depth:
            return

        x = node.x
        y = node.y
        half_width = (node.width - x)/2 + x
        half_height = (node.height - y)/2 +y
        
        objects = [[],[],[],[]]

        for obj in node.objects:
            if obj.x < half_width:
                if obj.y < half_height:
                    objects[0].append(obj)
                else:
                    objects[1].append(obj)
            else:
                if obj.y < half_height:
                    objects[2].append(obj)
                else:
                    objects[3].append(obj)
        
        node.nodes = [
            Node(x, y, half_width, half_height, objects[0],level),
            Node(x, half_height, half_width, node.height, objects[1],level),
            Node(half_width, node.y, node.width, half_height, objects[2],level),
            Node(half_width, half_height, node.width, node.height, objects[3],level)
        ]

        for child_node in node.nodes:
            self.build(child_node, depth, level+1)

    def get_in_region(self, x, y):
        level = self.root.nodes
        for node in level:
            if node.x < x and node.y < y and node.width > x and node.height > y:
                return node.objects
        return []