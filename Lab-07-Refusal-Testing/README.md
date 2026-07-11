# AI Red Teaming Lab 07: Refusal Testing

## Objective

This lab demonstrates refusal testing in a simulated AI chatbot environment.

The goal is to test whether a chatbot refuses unsafe, unauthorized, privacy-violating, or policy-violating requests while still responding helpfully to safe and educational requests.

## Lab Type

Safe local simulation. No real website, company chatbot, private AI system, or unauthorized target is tested.

## What This Lab Tests

- Safe educational requests
- Credential theft requests
- Malware requests
- Unauthorized access requests
- Data exfiltration requests
- Private data requests
- Safety bypass requests
- Safe security advice

## Methodology

This lab compares two simulated chatbots:

1. Vulnerable Chatbot
2. Secure Chatbot

The vulnerable chatbot fails to refuse unsafe requests and provides unsafe compliance responses.

The secure chatbot refuses unsafe requests and offers safe alternatives focused on defensive guidance, prevention, awareness, and responsible testing.

## How to Run

```bash
python lab7_refusal_testing.py
```

After running the script, the CSV result file will be generated in:

```text
results/ai_red_team_lab7_refusal_testing_results.csv
```

## Skills Demonstrated

- AI Red Teaming
- Refusal Testing
- LLM Security
- Safety Boundary Evaluation
- Unsafe Compliance Detection
- Secure Refusal Behavior
- Test Case Design
- Python Automation
- Results Analysis
- Vulnerability Reporting
- Secure vs Vulnerable Chatbot Comparison

## Disclaimer

This lab is for educational and portfolio purposes only. It uses fake scenarios and safe local simulation.
