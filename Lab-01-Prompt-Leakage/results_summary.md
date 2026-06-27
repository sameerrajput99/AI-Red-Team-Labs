# Lab 01 Results Summary: Prompt Leakage Testing

## Test Overview

This lab tested two simulated AI chatbots:

1. Vulnerable Chatbot
2. Secure Chatbot

The purpose was to check whether the chatbot reveals internal system instructions, internal policies, admin codes, or confidential notes when tested with red team prompts.

## Test Results

| Chatbot | Total Tests | Passed | Failed | Highest Severity |
|---|---:|---:|---:|---|
| Vulnerable Chatbot | 7 | 2 | 5 | High |
| Secure Chatbot | 7 | 7 | 0 | None |

## Key Finding

The vulnerable chatbot leaked internal system-level information when tested with prompts related to hidden instructions, system prompt extraction, internal policy extraction, debug mode abuse, and instruction override.

## Failed Test Categories

- Direct Prompt Leakage
- System Prompt Extraction
- Internal Policy Extraction
- Debug Mode Abuse
- Instruction Override

## Passed Secure Chatbot Behavior

The secure chatbot blocked requests related to:

- Hidden instructions
- System prompts
- Internal policies
- Admin codes
- Confidential information
- Instruction override attempts

## Conclusion

The vulnerable chatbot demonstrated prompt leakage behavior, while the secure chatbot successfully prevented sensitive information disclosure.

This lab demonstrates basic AI Red Teaming skills in prompt leakage testing, test case design, result analysis, and vulnerability reporting.
