# AI Red Teaming Lab 05: Hallucination Testing

## Objective

This lab demonstrates hallucination testing in a simulated AI chatbot environment.

The goal is to test whether a chatbot produces confident unsupported answers when the required information is not available in its knowledge base.

## Lab Type

Safe local simulation. No real website, company chatbot, private AI system, or unauthorized target is tested.

## What This Lab Tests

- Fabricated policy claims
- Fake product features
- Unverified statistics
- Fake citations
- Speculative future claims
- Fabricated incident claims
- Unsupported compliance claims

## Methodology

This lab compares two simulated chatbots:

1. Vulnerable Chatbot
2. Secure Chatbot

The vulnerable chatbot gives confident unsupported answers when information is missing.

The secure chatbot avoids guessing and clearly states when information cannot be verified.

## How to Run

```bash
python lab5_hallucination_testing.py
```

After running the script, the CSV result file will be generated in:

```text
results/ai_red_team_lab5_hallucination_testing_results.csv
```

## Skills Demonstrated

- AI Red Teaming
- Hallucination Testing
- LLM Security
- Unsupported Claim Detection
- Test Case Design
- Python Automation
- Results Analysis
- Vulnerability Reporting
- Secure vs Vulnerable Chatbot Comparison

## Disclaimer

This lab is for educational and portfolio purposes only. It uses fake data and safe local simulation.
