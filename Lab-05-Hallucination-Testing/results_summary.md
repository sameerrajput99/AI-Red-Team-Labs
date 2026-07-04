# Lab 05 Results Summary: Hallucination Testing

## Test Overview

This lab tested two simulated AI chatbots:

1. Vulnerable Chatbot
2. Secure Chatbot

The purpose was to check whether the chatbot gives confident unsupported answers when the required information is missing from the available knowledge base.

## Test Results

| Chatbot | Total Tests | Passed | Failed | Highest Severity |
|---|---:|---:|---:|---|
| Vulnerable Chatbot | 8 | 1 | 7 | High |
| Secure Chatbot | 8 | 8 | 0 | None |

## Key Finding

The vulnerable chatbot produced fabricated policies, fake product features, unverified statistics, fake citations, speculative claims, fabricated incidents, and unsupported compliance claims.

The secure chatbot avoided guessing and clearly stated when information could not be verified.

## Failed Test Categories

- Fabricated Policy
- Fake Product Feature
- Unverified Statistic
- Fake Citation
- Speculative Future Claim
- Fabricated Incident
- Unsupported Compliance Claim

## Secure Chatbot Behavior

The secure chatbot blocked hallucination risks by:

- Answering only from the available knowledge base
- Refusing to invent unsupported facts
- Avoiding fake citations
- Avoiding speculative predictions
- Asking for verified sources when needed
- Clearly stating uncertainty

## Conclusion

The vulnerable chatbot demonstrated hallucination behavior, while the secure chatbot successfully avoided unsupported claims.

This lab demonstrates practical AI Red Teaming skills in hallucination testing, result analysis, test case design, and vulnerability reporting.
