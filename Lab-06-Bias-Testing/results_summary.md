# Lab 06 Results Summary: Bias Testing

## Test Overview

This lab tested two simulated AI chatbots:

1. Vulnerable Chatbot
2. Secure Chatbot

The purpose was to check whether the chatbot gives unfair, stereotyped, or unequal responses based on identity-related attributes.

## Test Results

| Chatbot | Total Tests | Passed | Failed | Highest Severity |
|---|---:|---:|---:|---|
| Vulnerable Chatbot | 8 | 1 | 7 | High |
| Secure Chatbot | 8 | 8 | 0 | None |

## Key Finding

The vulnerable chatbot produced biased or unfair responses related to gender, age, language or nationality, disability, parental status, religious accommodation, and name or national origin.

The secure chatbot avoided unfair assumptions and focused on relevant qualifications, evidence, and role requirements.

## Failed Test Categories

- Gender Bias
- Age Bias
- Language/Nationality Bias
- Disability Bias
- Parental Status Bias
- Religious Accommodation Bias
- Name/National Origin Bias

## Secure Chatbot Behavior

The secure chatbot blocked bias risks by:

- Avoiding identity-based assumptions
- Refusing unfair comparisons
- Focusing on skills and job-relevant evidence
- Avoiding stereotypes
- Treating accommodations fairly
- Not using protected attributes for decision-making
- Encouraging evidence-based evaluation

## Conclusion

The vulnerable chatbot demonstrated biased decision-making behavior, while the secure chatbot successfully avoided unfair identity-based assumptions.

This lab demonstrates practical AI Red Teaming skills in bias testing, fairness evaluation, result analysis, test case design, and vulnerability reporting.
