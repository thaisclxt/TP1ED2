import 'dart:io';
import 'node.dart';

class Tree {
  Node _root;

  Tree() {
    this._root = null;
  }

  void add(int value) {
    _root = _add(value, _root);
  }

  Node _add(int value, Node node) {
    if (node == null) {
      return Node(value);
    }

    if (value < node.value) {
      node.left = _add(value, node.left);
    }

    if (value > node.value) {
      node.right = _add(value, node.right);
    }

    return node;
  }

  void remove(int value) {
    _root = _remove(value, _root);
  }

  Node _remove(int value, Node node) {
    if (node == null) return null;

    if (value != node.value) {
      if (value < node.value) {
        node.left = _remove(value, node.left);
      }

      if (value > node.value) {
        node.right = _remove(value, node.right);
      }
    } else {
      if (node.isLeaf) {
        return null;
      }

      if (node.isFull) {
        var newNode = _min(node.right);
        node.right = _remove(newNode.value, node.right);
        newNode.left = node.left;
        newNode.right = node.right;
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

  void inOrder() {
    _inOrder(_root);
    print("");
  }

  void _inOrder(Node node) {
    if (node == null) return;
    _inOrder(node.left);
    stdout.write("$node, ");
    _inOrder(node.right);
  }

  void preOrder() {
    _preOrder(_root);
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
