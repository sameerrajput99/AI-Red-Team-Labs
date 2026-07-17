# AI Red Teaming Lab 12: RAG Access Control Failure Testing

## Objective

This lab demonstrates RAG access control failure testing in a simulated retrieval-based AI chatbot.

The goal is to test whether a RAG chatbot enforces user permissions before returning retrieved document content.

## Lab Type

Safe local simulation. No real users, private documents, production RAG system, database, company data, or unauthorized target is tested.

## What This Lab Tests

- Public document access
- Employee-only document access
- Finance-only document access
- Admin-only document access
- Cross-tenant customer data access
- Role claim bypass attempts
- Authorized finance access
- Public support hours access

## Methodology

This lab compares two simulated RAG chatbot behaviors:

1. Vulnerable RAG Chatbot
2. Secure RAG Chatbot

The vulnerable RAG chatbot retrieves relevant documents and returns them without checking whether the user is authorized.

The secure RAG chatbot retrieves the document, validates the user's verified role and ownership permissions, and only returns content if access is allowed.

## How to Run

```bash
python lab12_rag_access_control_failure.py
```

After running the script, the CSV result file will be generated in:

```text
results/ai_red_team_lab12_rag_access_control_failure_results.csv
```

## Skills Demonstrated

- AI Red Teaming
- LLM Security
- RAG Security
- RAG Access Control Testing
- Role-Based Access Control Testing
- Document-Level Authorization
- Tenant Isolation Testing
- Permission Validation
- Secure RAG Response Design
- Test Case Design
- Python Automation
- Results Analysis
- Vulnerability Reporting
- Secure vs Vulnerable RAG Comparison
- GitHub Portfolio Documentation

## Disclaimer

This lab is for educational and portfolio purposes only. It uses fake users, fake documents, fake roles, and a safe local simulation.
