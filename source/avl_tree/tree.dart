import 'dart:io';
import 'node.dart';

class Tree {
  Node root;
  int _comparisons;

  int get comparisons => _comparisons;

  Tree() {
    this.root = null;
  }

  void add(int value) {
    if (search(value)[0]) return;

    root = _add(value, root, null);
  }

  Node _add(int value, Node node, Node parent) {
    if (node == null) {
      return Node(value, parent);
    }

    if (value < node.value) {
      node.left = _add(value, node.left, node);
    }

    if (value > node.value) {
      node.right = _add(value, node.right, node);
    }

    return node;
  }

  void remove(int value) {
    root = _remove(value, root, null);
  }

  Node _remove(int value, Node node, Node parent) {
    if (node == null) return null;

    if (value != node.value) {
      if (value < node.value) {
        node.left = _remove(value, node.left, node);
      }

      if (value > node.value) {
        node.right = _remove(value, node.right, node);
      }
    } else {
      if (node.isLeaf) {
        return null;
      }

      if (node.isFull) {
        var newNode = _min(node.right);
        node.right = _remove(newNode.value, node.right, node);
        newNode.left = node.left;
        newNode.right = node.right;
        newNode.parent = node.parent;
        return newNode;
      }

      if (node.left != null) return node.left;
      return node.right;
    }

    return node;
  }

  Node _min(Node node) {
    if (node.left == null) {
      return node;
    }
    return _min(node.left);
  }

  List search(int value) {
    _comparisons = 0;
    return [_search(value, root), _comparisons];
  }

  bool _search(int value, Node node) {
    _comparisons++;

    if (node == null) return false;

    if (node.value == value) return true;

    if (node.value > value) return _search(value, node.left);
    return _search(value, node.right);
  }

  void inOrder() {
    _inOrder(root);
    print("");
  }

  void _inOrder(Node node) {
    if (node == null) return;
    _inOrder(node.left);
    stdout.write("$node, ");
    _inOrder(node.right);
  }

  void preOrder() {
    _preOrder(root);
    print("");
  }

  void _preOrder(Node node) {
    if (node == null) return;

    stdout.write(node);
    stdout.write("{");
    _preOrder(node.left);
    stdout.write(", ");
    _preOrder(node.right);
    stdout.write("}");
  }
}
