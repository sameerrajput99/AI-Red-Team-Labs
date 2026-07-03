# AI Red Teaming Lab 04: Instruction Override Testing

## Objective

This lab demonstrates instruction override testing in a simulated AI chatbot environment.

The goal is to test whether a chatbot accepts user-provided instructions as higher priority than system-level rules.

## Lab Type

Safe local simulation. No real website, company chatbot, private AI system, or unauthorized target is tested.

## What This Lab Tests

- Conversation-level override
- Priority injection
- Role override
- Policy update abuse
- Safety disable attempt
- User-defined rule abuse
- Old rule removal

## Methodology

This lab compares two simulated chatbots:

1. Vulnerable Chatbot
2. Secure Chatbot

The vulnerable chatbot incorrectly accepts user instructions that attempt to change its role, disable safety checks, bypass policy requirements, or replace system-level rules.

The secure chatbot refuses attempts to override instruction hierarchy.

## How to Run

```bash
python lab4_instruction_override.py
```

After running the script, the CSV result file will be generated in:

```text
results/ai_red_team_lab4_instruction_override_results.csv
```

## Skills Demonstrated

- AI Red Teaming
- Instruction Override Testing
- Prompt Security Testing
- LLM Security
- Test Case Design
- Python Automation
- Results Analysis
- Vulnerability Reporting
- Secure vs Vulnerable Chatbot Comparison

## Disclaimer

This lab is for educational and portfolio purposes only. It uses fake internal data and safe local simulation.
