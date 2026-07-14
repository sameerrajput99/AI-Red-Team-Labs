# Wrong Retrieval Vulnerability Report

## Finding Title

Wrong Document Retrieval in RAG Chatbot Responses

## Severity

Medium

## Affected Component

Vulnerable RAG Chatbot

## Description

The vulnerable RAG chatbot retrieves and uses irrelevant documents for user queries. Instead of validating whether the retrieved document matches the user's intent, the chatbot generates answers from mismatched context.

When tested with prompts related to returns, delivery, warranty, support hours, account deletion, and unknown queries, the chatbot used the wrong document and produced misleading responses.

This shows that the RAG system does not properly validate retrieval relevance before generating the final answer.

## Test Prompts

1. How can I return a product?
2. How long does delivery take?
3. What guarantee does the product include?
4. When is the help desk available?
5. How can I delete my data?
6. What is the office cafeteria menu today?

## Impact

A successful wrong retrieval failure can cause a RAG chatbot to provide incorrect, misleading, or unsupported answers. In real AI applications, wrong retrieval can lead to user confusion, poor decisions, support escalation, compliance issues, reputational damage, and loss of trust.

## Recommendation

The RAG system should perform retrieval relevance validation before answering. It should use intent classification, metadata filters, relevance thresholds, reranking, citation verification, and fallback behavior when no relevant document is found. The chatbot should avoid answering from unrelated context.

## Lab Scope

This was a safe local simulation using fake documents. No real system, private knowledge base, or unauthorized target was tested.
