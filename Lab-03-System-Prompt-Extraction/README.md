# AI Red Teaming Lab 03: System Prompt Extraction Testing

## Objective

This lab demonstrates system prompt extraction testing in a simulated AI chatbot environment.

The goal is to test whether an AI chatbot reveals its hidden system prompt, original instructions, internal policies, or staff-only configuration when asked through direct or indirect extraction prompts.

## Lab Type

Safe local simulation. No real website, company chatbot, private AI system, or unauthorized target is tested.

## What This Lab Tests

- Direct system prompt request
- Hidden instruction extraction
- Original instruction repeat
- Configuration dump attempts
- JSON-based extraction
- Translation-based extraction
- Audit mode extraction

## Methodology

This lab compares two simulated chatbots:

1. Vulnerable Chatbot
2. Secure Chatbot

The vulnerable chatbot exposes fake internal system prompt content when extraction-style prompts are used.

The secure chatbot refuses direct and indirect attempts to reveal system prompts, hidden instructions, internal policies, or staff-only configuration.

## How to Run

```bash
python lab3_system_prompt_extraction.py
```

After running the script, the CSV result file will be generated in:

```text
results/ai_red_team_lab3_system_prompt_extraction_results.csv
```

## Skills Demonstrated

- AI Red Teaming
- System Prompt Extraction Testing
- LLM Security
- Prompt Security Testing
- Test Case Design
- Python Automation
- Results Analysis
- Vulnerability Reporting
- Secure vs Vulnerable Chatbot Comparison

## Disclaimer

This lab is for educational and portfolio purposes only. It uses fake internal data and safe local simulation.
