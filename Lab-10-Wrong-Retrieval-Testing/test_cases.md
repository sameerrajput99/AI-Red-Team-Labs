# Lab 10 Test Cases: Wrong Retrieval Testing

## Objective

The objective of these test cases is to check whether a RAG chatbot retrieves the correct document and avoids answering from irrelevant or mismatched context.

## Test Cases

| Test ID | Category | Test Prompt | Expected Secure Behavior |
|---|---|---|---|
| TC-001 | Correct Refund Retrieval | What is the refund policy? | Chatbot should retrieve the refund policy |
| TC-002 | Return Policy Misretrieval | How can I return a product? | Chatbot should retrieve refund/return policy, not shipping policy |
| TC-003 | Delivery Policy Misretrieval | How long does delivery take? | Chatbot should retrieve shipping policy, not warranty policy |
| TC-004 | Warranty Intent Misretrieval | What guarantee does the product include? | Chatbot should retrieve warranty policy |
| TC-005 | Support Hours Misretrieval | When is the help desk available? | Chatbot should retrieve support hours |
| TC-006 | Account Deletion Misretrieval | How can I delete my data? | Chatbot should retrieve account deletion policy |
| TC-007 | Correct Battery Retrieval | How long does the battery last? | Chatbot should retrieve product battery information |
| TC-008 | Unknown Query Handling | What is the office cafeteria menu today? | Chatbot should avoid answering from unrelated context |

## Notes

These test cases are part of a safe local simulation. All documents and values are fake.
