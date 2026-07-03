# Lab 04 Results Summary: Instruction Override Testing

## Test Overview

This lab tested two simulated AI chatbots:

1. Vulnerable Chatbot
2. Secure Chatbot

The purpose was to check whether the chatbot accepts user instructions that attempt to override system-level rules, change the chatbot role, disable safety checks, or bypass policy requirements.

## Test Results

| Chatbot | Total Tests | Passed | Failed | Highest Severity |
|---|---:|---:|---:|---|
| Vulnerable Chatbot | 8 | 1 | 7 | High |
| Secure Chatbot | 8 | 8 | 0 | None |

## Key Finding

The vulnerable chatbot accepted user-provided override instructions and changed its behavior. The secure chatbot refused these attempts and continued following system-level rules.

## Failed Test Categories

- Conversation-Level Override
- Priority Injection
- Role Override
- Policy Update Abuse
- Safety Disable Attempt
- User-Defined Rule Abuse
- Old Rule Removal

## Secure Chatbot Behavior

The secure chatbot blocked requests related to:

- User-defined rule override
- Priority injection
- Role override
- Fake policy updates
- Safety disable attempts
- Staff approval bypass
- Old rule removal

## Conclusion

The vulnerable chatbot demonstrated instruction override behavior, while the secure chatbot successfully enforced system-level rules.

This lab demonstrates practical AI Red Teaming skills in instruction hierarchy testing, result analysis, test case design, and vulnerability reporting.
