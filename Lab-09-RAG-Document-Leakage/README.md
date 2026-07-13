# AI Red Teaming Lab 09: RAG Document Leakage Testing

## Objective

This lab demonstrates RAG document leakage testing in a simulated AI chatbot environment.

The goal is to test whether a Retrieval-Augmented Generation system leaks confidential, internal, or access-restricted documents to an unauthorized user.

## Lab Type

Safe local simulation. No real company documents, private knowledge base, production RAG system, website, or unauthorized target is tested.

## What This Lab Tests

- Public document access
- Confidential HR document leakage
- Internal API configuration leakage
- Private contract document leakage
- Hidden document dump attempts
- Access control bypass attempts
- Citation-based document leakage
- Safe public FAQ retrieval

## Methodology

This lab compares two simulated RAG chatbot behaviors:

1. Vulnerable RAG Chatbot
2. Secure RAG Chatbot

The vulnerable RAG chatbot retrieves and exposes sensitive documents without authorization checks.

The secure RAG chatbot enforces document access control before using retrieved content in the answer. It only uses authorized public documents and refuses confidential or internal document requests.

## How to Run

```bash
python lab9_rag_document_leakage.py
```

After running the script, the CSV result file will be generated in:

```text
results/ai_red_team_lab9_rag_document_leakage_results.csv
```

## Skills Demonstrated

- AI Red Teaming
- LLM Security
- RAG Security
- RAG Document Leakage Testing
- Retrieval Security Testing
- Access Control Validation
- Sensitive Document Exposure Detection
- Secure RAG Response Design
- Test Case Design
- Python Automation
- Results Analysis
- Vulnerability Reporting
- Secure vs Vulnerable RAG Comparison

## Disclaimer

This lab is for educational and portfolio purposes only. It uses fake documents, fake secrets, and safe local simulation.
