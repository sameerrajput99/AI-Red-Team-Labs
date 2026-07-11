# AI Red Teaming Lab 08: Safety Boundary Testing

## Objective

This lab demonstrates safety boundary testing in a simulated AI chatbot environment.

The goal is to test whether a chatbot maintains safe behavior boundaries when a user tries to cross them using direct requests, policy override attempts, roleplay, hypothetical framing, obfuscation, or authority pressure.

## Lab Type

Safe local simulation. No real website, company chatbot, private AI system, or unauthorized target is tested.

## What This Lab Tests

- Safe educational requests
- Direct safety boundary violations
- Policy override attempts
- Roleplay-based boundary bypass
- Hypothetical framing
- Obfuscated or encoded request handling
- Authority pressure
- Safe defensive alternatives

## Methodology

This lab compares two simulated chatbots:

1. Vulnerable Chatbot
2. Secure Chatbot

The vulnerable chatbot fails when users try to cross safety boundaries.

The secure chatbot maintains safety boundaries and redirects users toward safe alternatives such as defensive guidance, policy design, monitoring, prevention, and responsible testing.

## How to Run

```bash
python lab8_safety_boundary_testing.py
```

After running the script, the CSV result file will be generated in:

```text
results/ai_red_team_lab8_safety_boundary_testing_results.csv
```

## Skills Demonstrated

- AI Red Teaming
- LLM Security
- AI Safety Testing
- Safety Boundary Testing
- Policy Boundary Evaluation
- Boundary Failure Detection
- Secure Refusal Behavior
- Safe Alternative Response Design
- Test Case Design
- Python Automation
- Results Analysis
- Vulnerability Reporting
- Secure vs Vulnerable Chatbot Comparison

## Disclaimer

This lab is for educational and portfolio purposes only. It uses fake scenarios and safe local simulation.
