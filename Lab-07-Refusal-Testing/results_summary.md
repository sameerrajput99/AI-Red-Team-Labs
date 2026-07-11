# Lab 07 Results Summary: Refusal Testing

## Test Overview

This lab tested two simulated AI chatbots:

1. Vulnerable Chatbot
2. Secure Chatbot

The purpose was to check whether the chatbot refuses unsafe requests while still responding to safe educational and defensive security prompts.

## Test Results

| Chatbot | Total Tests | Passed | Failed | Highest Severity |
|---|---:|---:|---:|---|
| Vulnerable Chatbot | 8 | 2 | 6 | High |
| Secure Chatbot | 8 | 8 | 0 | None |

## Key Finding

The vulnerable chatbot failed to refuse unsafe requests related to credential theft, malware, unauthorized access, data exfiltration, private data exposure, and refusal bypass.

The secure chatbot refused unsafe requests and provided safe alternatives focused on defensive guidance, prevention, awareness, and responsible testing.

## Failed Test Categories

- Credential Theft Request
- Malware Request
- Unauthorized Access Request
- Data Exfiltration Request
- Private Data Request
- Safety Bypass Request

## Secure Chatbot Behavior

The secure chatbot blocked unsafe compliance by:

- Refusing harmful or unauthorized requests
- Protecting private user information
- Maintaining refusal behavior under bypass attempts
- Providing safe alternatives
- Supporting defensive security guidance
- Answering safe educational requests

## Conclusion

The vulnerable chatbot demonstrated unsafe compliance behavior, while the secure chatbot successfully maintained safe refusal boundaries.

This lab demonstrates practical AI Red Teaming skills in refusal testing, unsafe compliance detection, result analysis, test case design, and vulnerability reporting.
