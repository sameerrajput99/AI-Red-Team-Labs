# Lab 11 Results Summary: Indirect Prompt Injection Testing

## Test Overview

This lab tested two simulated AI document summarizers:

1. Vulnerable Document Summarizer
2. Secure Document Summarizer

The purpose was to check whether the summarizer follows malicious or untrusted instructions hidden inside external document content.

## Test Results

| Chatbot | Total Tests | Passed | Failed | Highest Severity |
|---|---:|---:|---:|---|
| Vulnerable Document Summarizer | 8 | 2 | 6 | High |
| Secure Document Summarizer | 8 | 8 | 0 | None |

## Key Finding

The vulnerable document summarizer followed instructions embedded inside untrusted documents. It abandoned the summarization task, accepted role override attempts, exposed fake internal content, and treated document text as executable instructions.

The secure document summarizer ignored embedded instructions, treated document content as untrusted data, and continued the summarization task safely.

## Failed Test Categories

- Ignore Instruction Injection
- System Prompt Extraction Injection
- Task Abandonment Injection
- Fake Secret Extraction Injection
- Tool Action Injection
- Role Override Injection

## Secure Document Summarizer Behavior

The secure document summarizer prevented indirect prompt injection by:

- Treating external document content as untrusted data
- Ignoring embedded instructions inside documents
- Maintaining the intended summarization task
- Refusing hidden instruction extraction
- Avoiding fake secret exposure
- Not executing tool/action instructions from documents
- Not changing role based on document content

## Conclusion

The vulnerable document summarizer demonstrated indirect prompt injection behavior, while the secure document summarizer successfully separated trusted instructions from untrusted document content.

This lab demonstrates practical AI Red Teaming skills in indirect prompt injection testing, untrusted content handling, instruction/data separation, result analysis, test case design, and vulnerability reporting.
