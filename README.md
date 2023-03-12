<p align="center">
  <a href="https://python.org/" target="blank"><img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg" width="120" alt="Python Logo" /></a>
</p>
<h1 align="center">Coleções em Python</h1>

Este é um repositório que contém diferentes coleções implementadas em Python. As coleções são estruturas de dados que podem armazenar e manipular um conjunto de elementos. Cada coleção é implementada como uma classe Python, contendo métodos para manipular a coleção.


## Como usar?

Para usar as coleções neste repositório, basta clonar o repositório em sua máquina local e importar a classe correspondente ao tipo de coleção que você deseja usar. Por exemplo:
```
from collections.list import MyList
my_list = MyList([1, 2, 3])
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
```

## Tipos de coleções
O repositório contém as seguintes coleções implementadas:

### Lista (List)

Uma lista é uma coleção ordenada de elementos, em que cada elemento é identificado por um índice. A classe MyList implementa uma lista.

#### Métodos disponíveis

-   `append(item)`: adiciona um elemento no final da lista.
-   `insert(index, item)`: adiciona um elemento em uma posição específica da lista.
-   `remove(item)`: remove o elemento da lista.
-   `pop()`: remove e retorna o elemento no final da lista.
-   `pop(index)`: remove e retorna o elemento em uma posição específica da lista.
-   `index(item)`: retorna o índice do elemento na lista.
-   `count(item)`: retorna o número de vezes que o elemento aparece na lista.
-   `sort()`: ordena os elementos na lista.
-   `reverse()`: inverte a ordem dos elementos na lista.
-   `clear()`: remove todos os elementos da lista.

### Tupla (Tuple)

Uma tupla é uma coleção ordenada e imutável de elementos. A classe MyTuple implementa uma tupla.

#### Métodos disponíveis

-   `count(item)`: retorna o número de vezes que o elemento aparece na tupla.
-   `index(item)`: retorna o índice do elemento na tupla.

### Dicionário (Dictionary)

Um dicionário é uma coleção não ordenada de elementos, em que cada elemento é identificado por uma chave única. A classe MyDict implementa um dicionário.

#### Métodos disponíveis

-   `keys()`: retorna uma lista com as chaves do dicionário.
-   `values()`: retorna uma lista com os valores do dicionário.
-   `items()`: retorna uma lista com os pares (chave, valor) do dicionário.
-   `get(key, default=None)`: retorna o valor associado à chave, ou o valor default se a chave não existir.
-   `pop(key, default=None)`: remove e retorna o valor associado à chave, ou o valor default se a chave não existir.
-   `popitem()`: remove e retorna um par (chave, valor) aleatório do dicionário.
-   `clear()`: remove todos os elementos do dicionário.

### Conjunto (Set)

Um conjunto é uma coleção não ordenada e sem elementos duplicados. A classe MySet implementa um conjunto.

#### Métodos disponíveis

-   `add(item)`: adiciona um elemento ao conjunto.
-   `remove(item)`: remove o elemento do conjunto.
-   `discard(item)`: remove o elemento do conjunto, se ele existir.
-   `pop()`: remove e retorna um elemento aleatório do conjunto.
-   `clear()

## Autor

* **Programador (aluno)** - *Algoritmos* - [Antonio Moreira](https://github.com/antonio-moreira-prog)