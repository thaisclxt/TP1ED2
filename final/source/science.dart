import 'dart:io';

import 'avl_tree.dart';
import 'bs_tree.dart';

void main(List<String> args) {
  if (!verifyArgs(args)) return showHelp();

  final inputFile = File(args[0]);
  final searchFile = File(args[1]);

  var generatedNumbers = inputFile
      .readAsStringSync()
      .split(' ')
      .map((number) => int.parse(number))
      .toList();
  var searchGroups = searchFile
      .readAsLinesSync()
      .map((group) =>
          group.split(' ').map((number) => int.parse(number)).toList())
      .toList();

  final bsTree = BsTree();
  final avlTree = AvlTree();

  generatedNumbers.forEach((number) {
    bsTree.add(number);
    avlTree.add(number);
  });

  final comparisons = searchGroups.map((group) {
    return group
        .map((number) => [bsTree.search(number)[1], avlTree.search(number)[1]])
        .toList();
  }).toList();

  final medias = comparisons.map((group) {
    final sum = group.reduce(
        (value, element) => [value[0] + element[0], value[1] + element[1]]);
    return [sum[0] / 50, sum[1] / 50];
  }).toList();

  final result = File("result.txt");
  result.writeAsStringSync(exportResult(comparisons, medias));
}

String exportResult(List comparisons, List medias) {
  var result = " \t ABB \t ABB \t ABB \t AVL \t AVL \t AVL\n";
  result +=
      "MÉDIA: \t ${medias[0][0]} \t ${medias[1][0]} \t ${medias[2][0]} \t ${medias[0][1]} \t ${medias[1][1]} \t ${medias[2][1]}\n";
  result += " \t \t \t \t \t \t \n";
  result +=
      "# item \t Conj. Menor \t Conj. Maior \t Conj. Interno \t Conj. Menor \t Conj. Maior \t Conj. Interno\n";
  for (var index = 0; index < 50; index++) {
    result +=
        "${index + 1} \t ${comparisons[0][index][0]} \t ${comparisons[1][index][0]} \t ${comparisons[2][index][0]} \t ${comparisons[0][index][1]} \t ${comparisons[1][index][1]} \t ${comparisons[2][index][1]}\n";
  }

  return result;
}

bool verifyArgs(List<String> args) {
  switch (args.length) {
    case 0:
      print("ERRO: Não foram passados argumentos\n");
      return false;
    case 2:
      return verifyFiles(args);
    default:
      print("ERRO: A quantidade de argumentos não corresponde à esperada.");
      return false;
  }
}

bool verifyFiles(List<String> args) {
  var inputFile = File(args[0]);
  var searchFile = File(args[1]);

  if (!inputFile.existsSync()) {
    print("ERRO: O arquivo de inserção dos números não existe.\n");
    return false;
  }

  if (!searchFile.existsSync()) {
    print("ERRO: O arquivo com os conjuntos de busca não existe.\n");
    return false;
  }

  return true;
}

void showHelp() {
  print("---------------- AJUDA ----------------");
  print("Para executar o programa corretamente, utilize:");
  print("dart science.dart INPUT SEARCH");
  print("\nLembre-se de substituir \"INPUT\" pelo caminho relativo para o\n" +
      "\tarquivo que contém os 10.000 números, gerados pelo inputGenerator.");
  print("\nE de substituir \"SEARCH\" pelo caminho relativo para o\n" +
      "\tarquivo que contém os três conjuntos à serem buscados,\n" +
      "\ttambém gerados pelo inputGenerator.");
  print("---------------------------------------");
}
