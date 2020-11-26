import 'dart:io';
import 'node.dart';

class Tree {
  Node _root;
  int _comparisons;
  bool _needsBalance;

  int get comparisons => _comparisons;

  Tree() {
    this._root = null;
  }

  void add(int value) {
    _needsBalance = false;
    _root = _add(value, _root);
  }

  Node _add(int value, Node node) {
    if (node == null) {
      _needsBalance = true;
      return Node(value);
    }

    if (value == node.value) {
      return node;
    }

    if (value < node.value) {
      node.left = _add(value, node.left);

      if (_needsBalance) {
        switch (node.balance) {
          case 1:
            node.balance = 0;
            _needsBalance = false;
            break;
          case -1:
            node = _rebalanceLeft(node);
            break;
          default:
            node.balance = -1;
            break;
        }
      }
    } else if (value > node.value) {
      node.right = _add(value, node.right);

      if (_needsBalance) {
        switch (node.balance) {
          case 1:
            node = _rebalanceRight(node);
            break;
          case -1:
            node.balance = 0;
            _needsBalance = false;
            break;
          default:
            node.balance = 1;
            break;
        }
      }
    }

    return node;
  }

  Node _rebalanceLeft(Node node) {
    var leftChild = node.left;

    if (leftChild.balance == -1) {
      node.left = leftChild.right;
      leftChild.right = node;

      node.balance = 0;
      leftChild.balance = 0;
      _needsBalance = false;

      return leftChild;
    } else {
      var grandChild = leftChild.right;

      leftChild.right = grandChild.left;
      grandChild.left = leftChild;

      node.left = grandChild.right;
      grandChild.right = node;

      switch (grandChild.balance) {
        case -1:
          node.balance = 1;
          leftChild.balance = 0;

          break;
        case 1:
          leftChild.balance = -1;
          node.balance = 0;

          break;
        default:
          node.balance = 0;
          leftChild.balance = 0;

          break;
      }

      grandChild.balance = 0;
      _needsBalance = false;

      return grandChild;
    }
  }

  Node _rebalanceRight(Node node) {
    var rightChild = node.right;

    if (rightChild.balance == 1) {
      node.right = rightChild.left;
      rightChild.left = node;

      node.balance = 0;
      rightChild.balance = 0;
      _needsBalance = false;

      return rightChild;
    } else {
      var grandChild = rightChild.left;

      rightChild.left = grandChild.right;
      grandChild.right = rightChild;

      node.right = grandChild.left;
      grandChild.left = node;

      switch (grandChild.balance) {
        case 1:
          node.balance = -1;
          rightChild.balance = 0;

          break;
        case -1:
          rightChild.balance = 1;
          node.balance = 0;

          break;
        default:
          node.balance = 0;
          rightChild.balance = 0;

          break;
      }

      grandChild.balance = 0;
      _needsBalance = false;

      return grandChild;
    }
  }

  List search(int value) {
    _comparisons = 0;
    return [_search(value, _root), _comparisons];
  }

  bool _search(int value, Node node) {
    _comparisons++;

    if (node == null) return false;

    if (node.value == value) return true;

    if (node.value > value) return _search(value, node.left);
    return _search(value, node.right);
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
