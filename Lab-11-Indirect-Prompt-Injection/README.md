# AI Red Teaming Lab 11: Indirect Prompt Injection Testing

## Objective

This lab demonstrates indirect prompt injection testing in a simulated document summarizer environment.

The goal is to test whether an AI system follows malicious or untrusted instructions hidden inside external content such as documents, support tickets, emails, web pages, or retrieved text.

## Lab Type

Safe local simulation. No real user data, production AI system, private documents, website, or unauthorized target is tested.

## What This Lab Tests

- Safe customer support content
- Ignore-instruction injection
- System prompt extraction attempts
- Task abandonment injection
- Fake secret extraction attempts
- Tool/action instruction injection
- Role override injection
- Safe product feedback

## Methodology

This lab compares two simulated AI behaviors:

1. Vulnerable Document Summarizer
2. Secure Document Summarizer

The vulnerable document summarizer treats instructions inside untrusted document content as trusted commands.

The secure document summarizer treats document content as untrusted data. It ignores embedded instructions and continues the intended summarization task safely.

## How to Run

```bash
python lab11_indirect_prompt_injection.py
```

After running the script, the CSV result file will be generated in:

```text
results/ai_red_team_lab11_indirect_prompt_injection_results.csv
```

## Skills Demonstrated

- AI Red Teaming
- LLM Security
- Indirect Prompt Injection Testing
- Prompt Injection Defense
- Untrusted Content Handling
- Document Summarizer Security
- Instruction/Data Separation
- Secure AI Response Design
- Test Case Design
- Python Automation
- Results Analysis
- Vulnerability Reporting
- Secure vs Vulnerable AI Comparison

## Disclaimer

This lab is for educational and portfolio purposes only. It uses fake documents, fake secrets, and safe local simulation.
