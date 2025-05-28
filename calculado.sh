 #!/bin/bash

echo "Digite o primeiro número: "
read num1
echo "Digite o segundo número: "
read num2

echo "Escolha a operação (+, -, *, /): "
read operacao

case $operacao in
  +) resultado=$(echo "$num1 + $num2" | bc);;
  -) resultado=$(echo "$num1 - $num2" | bc);;
  \*) resultado=$(echo "$num1 * $num2" | bc);;
  /) resultado=$(echo "scale=2; $num1 / $num2" | bc);;
  *) echo "Operação inválida"; exit 1;;
esac

echo "Resultado: $resultado"
