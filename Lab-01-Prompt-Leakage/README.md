# AI Red Teaming Lab 01: Prompt Leakage Testing

## Objective
This lab demonstrates prompt leakage testing in a simulated AI chatbot environment.

The goal is to check whether a chatbot reveals hidden system instructions, internal policies, admin codes, or confidential notes when tested with red team prompts.

## Lab Type
Safe local simulation. No real website, real company system, or unauthorized target is tested.

## What This Lab Tests
- Hidden instruction extraction
- System prompt leakage
- Internal policy leakage
- Debug mode abuse
- Admin code request handling
- Instruction override attempts

## How It Works
The project compares two chatbots:

1. **Vulnerable Chatbot**
   - Leaks internal system prompt when certain prompts are used.

2. **Secure Chatbot**
   - Blocks requests for system prompts, internal policies, admin codes, and confidential information.

## Run the Lab

```bash
python lab1_prompt_leakage.py
```

## Output
The script prints test results in the terminal and generates a CSV report:

```text
results/ai_red_team_lab1_prompt_leakage_results.csv
```

## Example Finding

**Title:** Prompt Leakage in AI Chatbot

**Severity:** High

**Description:**  
The vulnerable chatbot reveals internal system instructions when the user asks for hidden instructions, system prompt, internal policy, or debug mode.

**Impact:**  
An attacker could extract internal instructions, admin codes, confidential notes, and system-level rules. This information could help the attacker design stronger prompt injection attacks or bypass guardrails.

**Recommendation:**  
The chatbot should never expose system prompts, internal policies, admin codes, or confidential notes. Sensitive instructions should be separated from user-visible responses. Input filtering, output validation, and strict access control should be applied.

## Skills Demonstrated
- AI Red Teaming
- Prompt leakage testing
- Prompt security testing
- Test case design
- Vulnerability reporting
- Secure chatbot comparison
- Python automation
