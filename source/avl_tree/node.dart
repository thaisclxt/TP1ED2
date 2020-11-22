class Node {
  int value;
  Node parent;
  Node left;
  Node right;

  Node(this.value, this.parent, {this.left = null, this.right = null});

  @override
  String toString() => this.value.toString();

  bool get isLeaf => this.left == null && this.right == null;
  bool get isFull => this.left != null && this.right != null;
}
