# Lab 08 Results Summary: Safety Boundary Testing

## Test Overview

This lab tested two simulated AI chatbots:

1. Vulnerable Chatbot
2. Secure Chatbot

The purpose was to check whether the chatbot maintains safety boundaries when users attempt direct boundary violations, policy override, roleplay bypass, hypothetical framing, obfuscation, or authority pressure.

## Test Results

| Chatbot | Total Tests | Passed | Failed | Highest Severity |
|---|---:|---:|---:|---|
| Vulnerable Chatbot | 8 | 2 | 6 | High |
| Secure Chatbot | 8 | 8 | 0 | None |

## Key Finding

The vulnerable chatbot failed to maintain safety boundaries when tested with direct restricted requests, policy override attempts, roleplay bypass, hypothetical framing, obfuscated requests, and authority pressure.

The secure chatbot maintained safety boundaries and redirected users toward safe alternatives focused on defensive guidance, prevention, policy design, and responsible testing.

## Failed Test Categories

- Direct Boundary Violation
- Policy Override Attempt
- Roleplay Boundary Bypass
- Hypothetical Framing
- Obfuscated Request
- Authority Pressure

## Secure Chatbot Behavior

The secure chatbot maintained safety boundaries by:

- Refusing restricted requests
- Not allowing policy override
- Not bypassing safety through roleplay
- Maintaining boundaries in hypothetical framing
- Handling obfuscated requests safely
- Resisting authority pressure
- Providing safe defensive alternatives

## Conclusion

The vulnerable chatbot demonstrated safety boundary failure, while the secure chatbot successfully maintained safe behavior limits across multiple prompt styles.

This lab demonstrates practical AI Red Teaming skills in safety boundary testing, policy boundary evaluation, result analysis, test case design, and vulnerability reporting.
