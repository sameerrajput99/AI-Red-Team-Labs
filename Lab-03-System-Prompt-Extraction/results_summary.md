# Lab 03 Results Summary: System Prompt Extraction Testing

## Test Overview

This lab tested two simulated AI chatbots:

1. Vulnerable Chatbot
2. Secure Chatbot

The purpose was to check whether the chatbot reveals hidden system prompts, original instructions, internal policies, or staff-only configuration when tested with extraction-style prompts.

## Test Results

| Chatbot | Total Tests | Passed | Failed | Highest Severity |
|---|---:|---:|---:|---|
| Vulnerable Chatbot | 8 | 1 | 7 | High |
| Secure Chatbot | 8 | 8 | 0 | None |

## Key Finding

The vulnerable chatbot exposed fake internal system prompt content when tested with direct and indirect extraction attempts. The secure chatbot blocked those attempts and refused to reveal system-level information.

## Failed Test Categories

- Direct System Prompt Request
- Hidden Instruction Extraction
- Original Instruction Repeat
- Configuration Dump
- JSON Extraction
- Translation-Based Extraction
- Audit Mode Extraction

## Secure Chatbot Behavior

The secure chatbot blocked requests related to:

- System prompts
- Hidden instructions
- Original instructions
- Internal policies
- Staff-only configuration
- JSON-based extraction
- Translation-based extraction
- Audit-mode extraction

## Conclusion

The vulnerable chatbot demonstrated system prompt extraction behavior, while the secure chatbot successfully prevented internal instruction disclosure.

This lab demonstrates practical AI Red Teaming skills in system prompt extraction testing, result analysis, test case design, and vulnerability reporting.
