class Node {
  int value;
  int balance;
  Node left;
  Node right;

  Node(this.value, {this.left = null, this.right = null}) {
    balance = 0;
  }

  @override
  String toString() => this.value.toString();

  bool get isLeaf => this.left == null && this.right == null;
  bool get isFull => this.left != null && this.right != null;
}
