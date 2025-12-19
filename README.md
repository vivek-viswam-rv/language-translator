# Neural Machine Translation: French → English

This repository contains the complete implementation of a Neural Machine Translation (NMT) system for translating French text into English. The project explores and compares multiple deep learning architectures, including GRU-based and Transformer-based models, to evaluate their effectiveness on the Europarl v7 French–English dataset.

## Project Overview

Neural Machine Translation is a sequence-to-sequence learning task where a model learns to map sentences from a source language to a target language. In this project, we build an end-to-end translation pipeline that includes data preprocessing, tokenization, model training, hyperparameter tuning, and evaluation using BLEU score.

The goal of this project is to identify the best-performing architecture for French-to-English translation under computational constraints.

## Models Implemented

- **GRU Seq2Seq with Attention**
  - Bidirectional encoder
  - Bahdanau (additive) attention mechanism
  - Subword tokenization using SentencePiece (BPE)

- **Transformer Models**
  - Multi-head self-attention
  - Encoder–decoder architecture
  - Positional embeddings
  - Trained with and without rare-word replacement using `<UNKN>`

## Dataset

- **Europarl v7 French–English Parallel Corpus**
- Sentence-aligned parliamentary proceedings
- Trained on a subset of 200,000 sentence pairs
- Split into training, validation, and test sets

## Preprocessing

- Text normalization and cleaning
- Lowercasing and whitespace normalization
- Subword tokenization (for GRU models)
- Word-level tokenization (for Transformer models)
- Sequence padding and truncation

## Evaluation

Model performance is evaluated using **BLEU score** on a held-out test set.

| Model           | Test BLEU (%) |
|-----------------|---------------|
| GRU             | 21.73         |
| Transformer 1   | 28.85         |
| Transformer 2   | 55.68         |

## Training Details

- Loss Function: Categorical Cross-Entropy
- Optimizer: Adam
- Teacher Forcing with decaying schedule
- Gradient Clipping for training stability
