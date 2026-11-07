# Reflexão sobre o processo de desenvolvimento com Scrum

**Atividade:** Parada Obrigatória 2 — Bug Hunter & TDD Calculator

Esta atividade foi individual, então os papéis do Scrum (Product Owner, Scrum Master e time de desenvolvimento) ficaram todos comigo. O enunciado funcionou como as necessidades do cliente, e o professor, como o stakeholder que avalia a entrega. Mesmo assim, foi possível reconhecer os elementos do framework no meu fluxo de trabalho.

## Como o Scrum apareceu na atividade

| Elemento do Scrum | Na atividade |
|---|---|
| **Product Backlog** | A lista de defeitos do `Calculadora.py`, registrada no `Bugs.md` com severidade e status. |
| **Sprint** | O período de 06/11/2026 a 09/11/2026, com prazo fixo de entrega. |
| **Meta da Sprint** | Identificar e relatar os bugs, corrigir um deles com TDD e entregar tudo no GitHub. |
| **Sprint Backlog** | As etapas do enunciado: copiar o código, achar os bugs, escrever os relatórios, aplicar o TDD, documentar e fazer o push. |
| **Incremento** | O código com o BUG-01 e o BUG-13 corrigidos, os testes e a documentação (`Bugs.md` e `Correcao.md`). |
| **Definição de Pronto** | Teste passando, documentação da correção, status do bug atualizado, commit e push no repositório público. |

## Transparência, inspeção e adaptação

- **Transparência:** o estado do trabalho ficou visível no `Bugs.md` (com status de cada bug), nas evidências da pasta `evidencias/` e no histórico de commits, que mostra cada fase do TDD.
- **Inspeção:** os testes automatizados inspecionavam o código a cada passo. O teste vermelho provou o defeito e o teste verde provou a correção. Também revisei o `git diff` antes de cada commit.
- **Adaptação:** ao escrever o primeiro teste, descobri que o módulo executava a calculadora ao ser importado, o que impedia o pytest de rodar. Esse impedimento virou um novo item do backlog (BUG-13), foi registrado e corrigido antes de seguir com o BUG-01. O backlog não é fixo: o que se aprende durante a sprint muda o plano.

## Scrum e TDD

O TDD combina bem com o Scrum porque os dois trabalham em ciclos curtos e com feedback rápido. Cada ciclo (teste que falha, correção mínima, refatoração) entrega um pequeno incremento verificável, em vez de uma grande mudança que só seria testada no fim. Os commits pequenos e separados por fase também deixam o progresso rastreável, como o Scrum pede.

## Priorização e escopo

Com 13 bugs no backlog e uma sprint curta, não era possível, nem pedido, corrigir todos. Escolhi o BUG-01 (adição retornando `2x + y`) por ser **crítico**: é uma operação básica que erra sem avisar. Priorizar pelo maior valor e impacto é o que o Scrum recomenda para o Product Backlog. O BUG-13 entrou na sprint porque bloqueava o trabalho.

Os bugs 02 a 12 não foram corrigidos e ficam como backlog da próxima sprint. Para cada um deles, deixei testes no arquivo `test_bugs_extra.py` descrevendo o comportamento esperado. Esses testes são os critérios de aceite de uma futura correção, e a suíte avisa quando um deles passar.

## Retrospectiva

**O que funcionou bem**
- Registrar os bugs com um modelo único deixou o relatório consistente e fácil de revisar.
- Escrever o teste antes da correção deixou claro o que significava "corrigido".
- Documentar durante o trabalho, e não só no fim, evitou perder evidências.

**O que dificultou**
- Eu não sabia que o pytest só encontra arquivos cujo nome começa com `test_`. Nomeei o arquivo de forma diferente e o pytest rodou sem coletar nenhum teste. A causa não era óbvia, e passei por isso antes de entender.
- Como a atividade foi individual, não houve Daily, revisão por pares nem papéis separados. A revisão de código por colegas, citada no enunciado, não foi possível. A autorrevisão do `git diff` substituiu essa etapa, mas um segundo par de olhos teria encontrado mais coisas.

**O que faria diferente na próxima sprint**
- Rodar um teste simples de importação logo no início, antes de escrever qualquer teste de verdade, para descobrir cedo problemas de estrutura como o do BUG-13.
- Estimar o tamanho de cada bug antes de escolher qual corrigir, e planejar quantos cabem na sprint.
- Pedir a revisão de um colega no momento do commit, para ter inspeção externa do código.

## Conclusão

A atividade mostrou, em pequena escala, como o Scrum organiza um trabalho de desenvolvimento: um backlog priorizado, uma meta clara para a sprint, entregas verificáveis e adaptação quando algo inesperado aparece. Aplicado junto com TDD e controle de versão no Git, o resultado foi um processo em que cada decisão deixou um rastro auditável (relatórios, testes e commits).