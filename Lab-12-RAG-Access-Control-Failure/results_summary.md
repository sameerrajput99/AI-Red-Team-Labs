# Lab 12 Results Summary: RAG Access Control Failure Testing

## Test Overview

This lab tested two simulated RAG chatbots:

1. Vulnerable RAG Chatbot
2. Secure RAG Chatbot

The purpose was to check whether the RAG chatbot enforces user permissions before returning retrieved document content.

## Test Results

| Chatbot | Total Tests | Passed | Failed | Highest Severity |
|---|---:|---:|---:|---|
| Vulnerable RAG Chatbot | 8 | 3 | 5 | High |
| Secure RAG Chatbot | 8 | 8 | 0 | None |

## Key Finding

The vulnerable RAG chatbot retrieved relevant documents but returned restricted content without checking whether the user was authorized. It exposed employee-only, finance-only, admin-only, and cross-tenant customer content.

The secure RAG chatbot retrieved documents, checked role and ownership permissions, refused unauthorized requests, and returned content only when access was allowed.

## Failed Test Categories

- Employee-Only Document Access
- Finance Document Access
- Admin Document Access
- Cross-Tenant Customer Data Access
- Role Claim Bypass Attempt

## Secure RAG Chatbot Behavior

The secure RAG chatbot prevented access control failure by:

- Checking user role before returning retrieved content
- Enforcing document-level permissions
- Enforcing customer ownership checks
- Preventing cross-tenant data exposure
- Refusing role claim bypass attempts
- Returning public documents safely
- Returning restricted documents only to authorized roles
- Providing safe refusal responses for unauthorized access

## Conclusion

The vulnerable RAG chatbot demonstrated access control failure because it treated retrieval as permission. The secure RAG chatbot separated retrieval from authorization and enforced access control before answering.

This lab demonstrates practical AI Red Teaming skills in RAG security testing, access control validation, document-level authorization, tenant isolation testing, result analysis, test case design, and vulnerability reporting.
