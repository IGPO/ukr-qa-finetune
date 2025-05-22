# 🧠 Ukrainian Academic QA Fine-Tuning

This project demonstrates a complete pipeline for fine-tuning a language model to generate questions based on a Ukrainian-language scientific dissertation.

## 📌 Features
- PDF text extraction and cleaning
- Chunking and QA dataset generation
- Instruction-style dataset formatting
- Fine-tuning with 🤗 Transformers + PEFT
- Optional bilingual mode (Ukrainian + English)
- Colab notebooks for reproducibility

## 🚀 Try it now

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO/blob/main/notebooks/extract_text.ipynb)

## 🗂 Project structure
ukr-qa-finetune/
├── data/ # Raw and processed data
├── notebooks/ # Jupyter notebooks for extraction and generation
│ └── extract_text.ipynb
├── scripts/ # Training, evaluation, inference
├── models/ # (optional) checkpoints
├── README.md
└── requirements.txt

## 🛠 How to run locally

```bash
pip install -r requirements.txt
python scripts/train.py
📚 License
MIT
