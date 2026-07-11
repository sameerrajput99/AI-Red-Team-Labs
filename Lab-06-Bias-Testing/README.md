# AI Red Teaming Lab 06: Bias Testing

## Objective

This lab demonstrates bias testing in a simulated AI chatbot environment.

The goal is to test whether a chatbot produces unfair, stereotyped, or unequal responses based on identity-related or protected attributes instead of relevant evidence.

## Lab Type

Safe local simulation. No real website, company chatbot, private AI system, or unauthorized target is tested.

## What This Lab Tests

- Gender bias
- Age bias
- Language or nationality bias
- Disability bias
- Parental status bias
- Religious accommodation bias
- Name or national origin bias
- Fair decision-making behavior

## Methodology

This lab compares two simulated chatbots:

1. Vulnerable Chatbot
2. Secure Chatbot

The vulnerable chatbot makes unfair assumptions or gives unequal recommendations based on identity-related attributes.

The secure chatbot avoids using protected or identity-related attributes and focuses on relevant qualifications, evidence, and role requirements.

## How to Run

```bash
python lab6_bias_testing.py
```

After running the script, the CSV result file will be generated in:

```text
results/ai_red_team_lab6_bias_testing_results.csv
```

## Skills Demonstrated

- AI Red Teaming
- Bias Testing
- LLM Security
- Responsible AI Testing
- Fairness Evaluation
- Test Case Design
- Python Automation
- Results Analysis
- Vulnerability Reporting
- Secure vs Vulnerable Chatbot Comparison

## Disclaimer

This lab is for educational and portfolio purposes only. It uses fake scenarios and safe local simulation.
