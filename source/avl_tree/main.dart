import 'tree.dart';

main() {
  var tree = Tree();
  //12 5 18 2 15 19 17
  tree.add(12);
  tree.add(5);
  tree.add(18);
  tree.add(2);
  tree.add(15);
  tree.add(19);
  tree.add(17);
  tree.preOrder();
  tree.remove(18);
  tree.preOrder();
  print(tree.search(19));
  print(tree.search(8));
  tree.add(19);
  tree.preOrder();
  print(tree.root.right.parent);
}
