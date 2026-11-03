# 🃏 Blackjack — Jogo de 21


## 👥 Participantes

| Nome | Matrícula |
|---|---|
| Everaldo Ferreira Santana | 2026001409 |
| Gabriel Marx Pepe Araujo | 2026016368 |
| Giovanni Ramos Andrade | 2026004465 |
| Joao Guilherme Sousa dos Santos | 2026002943 |

## 📌 Sobre o projeto

O **Blackjack**, também conhecido como 21, é um jogo de cartas em que o jogador enfrenta o dealer (banca), buscando obter uma pontuação maior que a dele sem ultrapassar 21 pontos.

Este projeto foi desenvolvido em Python como parte de uma atividade acadêmica, com o objetivo de aplicar conceitos de Programação Orientada a Objetos.

O jogo possui uma interface gráfica e uma interface de terminal, ambas utilizando o mesmo modelo responsável pelas regras e pela lógica da partida (sendo independentes entr si)

## 📂 Estrutura do projeto

```text
Blackjack/
├── card.py
├── card_collections.py
├── player.py
├── blackjack.py
├── exceptions.py
├── blackjack_terminal.py
├── blackjack_gui.py
└── README.md
```

## 🚀 Como executar

### Interface gráfica

```bash
python blackjack_gui.py
```

### Interface de terminal

```bash
python blackjack_terminal.py
```

> É necessário ter o Python instalado para executar o projeto.

## 📖 Regras do jogo

1. O jogador recebe duas cartas, enquanto o dealer recebe uma carta aberta e uma oculta.
2. O jogador pode pedir cartas ou parar.
3. Se ultrapassar 21 pontos, perde a partida.
4. Quando o jogador para, o dealer revela sua carta oculta e compra cartas.
5. Vence quem tiver a maior pontuação sem ultrapassar 21.
6. Se os dois participantes tiverem a mesma pontuação, ocorre um empate.

## 🎯 Objetivo acadêmico

Aplicar os conceitos de orientação a objetos na construção de um jogo, mantendo a separação entre a lógica do sistema e suas interfaces.

---

**Projeto acadêmico — Blackjack (21)**