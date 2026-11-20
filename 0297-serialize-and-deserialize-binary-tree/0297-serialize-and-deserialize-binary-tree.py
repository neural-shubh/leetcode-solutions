
class Codec:

    def serialize(self, root):
        values = []

        def preorder(node):
            if node is None:
                values.append("null")
                return

            values.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(values)

    def deserialize(self, data):
        values = iter(data.split(","))

        def build():
            value = next(values)

            if value == "null":
                return None

            node = TreeNode(int(value))
            node.left = build()
            node.right = build()

            return node

        return build()
