# Bug Hunter & TDD Calculator

Atividade **Parada Obrigatória 2** (SENAI CIMATEC), feita individualmente.

O projeto parte de uma calculadora científica simples em Python (`Calculadora.py`) que contém defeitos. O trabalho consiste em encontrar esses defeitos, relatá-los e corrigir um deles aplicando TDD, com todo o processo versionado no Git.

## Objetivo

- Praticar a identificação de defeitos e o relato detalhado de bugs.
- Praticar a metodologia TDD (teste que falha, correção mínima e refatoração).
- Usar o Git e o GitHub para controle de versão e entrega.
- Refletir sobre o processo de desenvolvimento usando o framework Scrum.

## Resultado

- **13 bugs** identificados e relatados (BUG-01 a BUG-13).
- **BUG-01** (adição retornava `2x + y`) corrigido com TDD.
- **BUG-13** (importar o módulo executava a calculadora) corrigido, por impedir os testes automatizados.
- **BUG-02 a BUG-12** documentados, cada um com testes que descrevem o comportamento esperado.

## Relatórios e arquivos

| Arquivo | O que contém |
|---|---|
| [`Bugs.md`](Bugs.md) | Relatório dos 13 bugs: título, localização, descrição, passos para reproduzir, resultado esperado vs. obtido, evidências, severidade, sugestão de correção, data e status. |
| [`Correcao.md`](Correcao.md) | Como o BUG-01 foi corrigido com TDD, passo a passo, incluindo o tratamento do BUG-13 e os testes dos demais bugs. |
| [`Reflexao_Scrum.md`](Reflexao_Scrum.md) | Reflexão sobre o processo de desenvolvimento usando o Scrum. |
| [`Calculadora.py`](Calculadora.py) | Código da calculadora científica, com as correções do BUG-01 e do BUG-13. |
| [`test_calculadora.py`](test_calculadora.py) | Testes do BUG-01, usados no ciclo TDD. |
| [`test_bugs_extra.py`](test_bugs_extra.py) | Testes dos bugs 02 a 12, que falham de propósito (`xfail`) enquanto os bugs existirem. |
| [`evidencias/`](evidencias/) | Prints do terminal que comprovam cada bug e as fases do TDD. |

## Como executar

Pré-requisitos: Python 3, Git e as bibliotecas NumPy e pytest.

```bash
python -m venv venv
venv\Scripts\activate        # Windows (no Linux/macOS: source venv/bin/activate)
pip install numpy pytest
```

Executar a calculadora:

```bash
python Calculadora.py
```

Executar os testes:

```bash
python -m pytest -v
```

Resultado esperado: `4 passed, 41 xfailed`. Os 41 `xfailed` são os testes dos bugs ainda não corrigidos. Para ver esses testes falhando de verdade, use `python -m pytest --runxfail`.