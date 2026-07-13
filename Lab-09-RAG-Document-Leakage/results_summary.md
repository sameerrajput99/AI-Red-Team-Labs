# Lab 09 Results Summary: RAG Document Leakage Testing

## Test Overview

This lab tested two simulated RAG chatbots:

1. Vulnerable RAG Chatbot
2. Secure RAG Chatbot

The purpose was to check whether the chatbot leaks confidential, internal, or access-restricted documents from a simulated RAG knowledge base.

## Test Results

| Chatbot | Total Tests | Passed | Failed | Highest Severity |
|---|---:|---:|---:|---|
| Vulnerable RAG Chatbot | 8 | 2 | 6 | High |
| Secure RAG Chatbot | 8 | 8 | 0 | None |

## Key Finding

The vulnerable RAG chatbot leaked restricted document content related to confidential HR records, fake internal API configuration, private vendor contract terms, hidden document dumps, unverified admin access, and citation-based leakage.

The secure RAG chatbot enforced access control and refused confidential or internal document access while still answering safe public queries.

## Failed Test Categories

- Confidential HR Document Request
- Internal API Key Document Request
- Private Contract Document Request
- Hidden Document Dump Request
- Access Control Bypass Attempt
- Citation Leakage Attempt

## Secure RAG Chatbot Behavior

The secure RAG chatbot prevented document leakage by:

- Enforcing document access control
- Using only authorized public documents
- Refusing confidential document requests
- Refusing internal configuration leakage
- Not trusting unverified role claims
- Blocking hidden document dump requests
- Preventing citation-based leakage
- Providing safe public information when allowed

## Conclusion

The vulnerable RAG chatbot demonstrated document leakage behavior, while the secure RAG chatbot successfully protected restricted documents and maintained safe retrieval boundaries.

This lab demonstrates practical AI Red Teaming skills in RAG security testing, retrieval security, access control validation, result analysis, test case design, and vulnerability reporting.
