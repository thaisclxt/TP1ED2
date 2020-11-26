import 'tree.dart';

main() {
  var tree = Tree();
  var numbers = [7, 17, 78, 35, 49, 99, 71, 32, 95, 55, 84, 31, 29];
  numbers.forEach((number) {
    tree.add(number);
  });
  tree.preOrder();
  tree.inOrder();
}
