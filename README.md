# AI Red Teaming Lab 02: Prompt Injection Testing

## Objective

This lab demonstrates prompt injection testing in a simulated AI chatbot environment.

The goal is to test whether a chatbot follows malicious user instructions that try to override system-level rules.

## Lab Type

Safe local simulation. No real website, real company system, private AI system, or unauthorized target is tested.

## What This Lab Tests

- Direct prompt injection
- Developer mode abuse
- Rule override attempts
- Admin roleplay attacks
- Internal data extraction attempts
- Safety bypass attempts

## Methodology

This lab compares two simulated chatbots:

1. Vulnerable Chatbot
2. Secure Chatbot

The vulnerable chatbot incorrectly follows malicious user instructions and exposes fake internal system data.

The secure chatbot detects suspicious prompt injection patterns and refuses to reveal internal information.

## How to Run

```bash
python lab2_prompt_injection.py
```

After running the script, the CSV result file will be generated in:

```text
results/ai_red_team_lab2_prompt_injection_results.csv
```

## Skills Demonstrated

- AI Red Teaming
- Prompt Injection Testing
- LLM Security
- Test Case Design
- Python Automation
- Vulnerability Reporting
- Secure vs Vulnerable Chatbot Comparison

## Disclaimer

This lab is for educational and portfolio purposes only. It uses fake internal data and safe local simulation.
