# Lab 02 Results Summary: Prompt Injection Testing

## Test Overview

This lab tested two simulated AI chatbots:

1. Vulnerable Chatbot
2. Secure Chatbot

The purpose was to check whether the chatbot follows malicious user instructions that attempt to override system-level rules.

## Test Results

| Chatbot | Total Tests | Passed | Failed | Highest Severity |
|---|---:|---:|---:|---|
| Vulnerable Chatbot | 7 | 1 | 6 | High |
| Secure Chatbot | 7 | 7 | 0 | None |

## Key Finding

The vulnerable chatbot followed prompt injection attempts and exposed fake internal system-level information. This happened when the user asked it to ignore previous instructions, enable developer mode, forget its rules, act as admin, print internal data, or bypass safety rules.

## Failed Test Categories

- Direct Prompt Injection
- Developer Mode Abuse
- Rule Override
- Admin Roleplay
- Internal Data Extraction
- Bypass Attempt

## Secure Chatbot Behavior

The secure chatbot blocked requests related to:

- Instruction override
- Developer mode abuse
- Admin roleplay
- Internal data exposure
- Safety bypass attempts
- System rule disclosure

## Conclusion

The vulnerable chatbot demonstrated prompt injection behavior, while the secure chatbot successfully blocked malicious instruction override attempts.

This lab demonstrates practical AI Red Teaming skills in prompt injection testing, test case design, result analysis, and vulnerability reporting.
