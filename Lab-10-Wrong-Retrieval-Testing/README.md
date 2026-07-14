# AI Red Teaming Lab 10: Wrong Retrieval Testing

## Objective

This lab demonstrates wrong retrieval testing in a simulated RAG chatbot environment.

The goal is to test whether a Retrieval-Augmented Generation system retrieves and answers from the correct document, or whether it uses irrelevant context and generates misleading answers.

## Lab Type

Safe local simulation. No real company documents, private knowledge base, production RAG system, website, or unauthorized target is tested.

## What This Lab Tests

- Correct public document retrieval
- Return policy misretrieval
- Delivery policy misretrieval
- Warranty intent misretrieval
- Support hours misretrieval
- Account deletion misretrieval
- Correct product information retrieval
- Unknown query handling

## Methodology

This lab compares two simulated RAG chatbot behaviors:

1. Vulnerable RAG Chatbot
2. Secure RAG Chatbot

The vulnerable RAG chatbot uses weak retrieval logic and answers from irrelevant documents.

The secure RAG chatbot maps user intent to the correct document and performs a relevance check before answering.

## How to Run

```bash
python lab10_wrong_retrieval_testing.py
```

After running the script, the CSV result file will be generated in:

```text
results/ai_red_team_lab10_wrong_retrieval_testing_results.csv
```

## Skills Demonstrated

- AI Red Teaming
- LLM Security
- RAG Security
- Wrong Retrieval Testing
- Retrieval Relevance Validation
- Context Quality Testing
- RAG Evaluation
- Secure RAG Response Design
- Test Case Design
- Python Automation
- Results Analysis
- Vulnerability Reporting
- Secure vs Vulnerable RAG Comparison

## Disclaimer

This lab is for educational and portfolio purposes only. It uses fake documents and safe local simulation.
