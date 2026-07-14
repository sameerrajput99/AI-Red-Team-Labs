# Lab 10 Results Summary: Wrong Retrieval Testing

## Test Overview

This lab tested two simulated RAG chatbots:

1. Vulnerable RAG Chatbot
2. Secure RAG Chatbot

The purpose was to check whether the chatbot retrieves the correct document or answers from irrelevant and mismatched context.

## Test Results

| Chatbot | Total Tests | Passed | Failed | Highest Severity |
|---|---:|---:|---:|---|
| Vulnerable RAG Chatbot | 8 | 2 | 6 | Medium |
| Secure RAG Chatbot | 8 | 8 | 0 | None |

## Key Finding

The vulnerable RAG chatbot used irrelevant retrieved documents for several user queries. It answered return-related, delivery-related, warranty-related, support-related, account-deletion-related, and unknown questions using mismatched context.

The secure RAG chatbot retrieved the correct documents when available and avoided answering from unrelated context when no relevant document was found.

## Failed Test Categories

- Return Policy Misretrieval
- Delivery Policy Misretrieval
- Warranty Intent Misretrieval
- Support Hours Misretrieval
- Account Deletion Misretrieval
- Unknown Query Handling

## Secure RAG Chatbot Behavior

The secure RAG chatbot avoided wrong retrieval by:

- Mapping user intent to the correct document topic
- Checking retrieval relevance before answering
- Avoiding answers from unrelated documents
- Handling unknown queries safely
- Using relevant context only
- Reducing misleading or unsupported responses

## Conclusion

The vulnerable RAG chatbot demonstrated wrong retrieval behavior, while the secure RAG chatbot successfully used relevant documents and avoided mismatched context.

This lab demonstrates practical AI Red Teaming skills in RAG security testing, retrieval relevance validation, context quality testing, result analysis, test case design, and vulnerability reporting.
