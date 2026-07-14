import csv
from datetime import datetime
from pathlib import Path

WRONG_RETRIEVAL_MARKERS = [
    "WRONG_DOCUMENT_USED",
    "IRRELEVANT_CONTEXT_USED",
    "MISMATCHED_POLICY_ANSWER",
    "WRONG_PRODUCT_INFO_USED",
    "UNSUPPORTED_FROM_RETRIEVAL",
    "LOW_RELEVANCE_ANSWER"
]


documents = [
    {
        "doc_id": "DOC-001",
        "title": "Refund Policy",
        "topic": "refund",
        "content": "REFUND_POLICY: Customers can request a refund within 14 days with proof of purchase."
    },
    {
        "doc_id": "DOC-002",
        "title": "Shipping Policy",
        "topic": "shipping",
        "content": "SHIPPING_POLICY: Standard shipping takes 3 to 5 business days."
    },
    {
        "doc_id": "DOC-003",
        "title": "Warranty Policy",
        "topic": "warranty",
        "content": "WARRANTY_POLICY: Products include a 1-year limited warranty for manufacturing defects."
    },
    {
        "doc_id": "DOC-004",
        "title": "Support Hours",
        "topic": "support",
        "content": "SUPPORT_HOURS: Customer support is available Monday to Friday, 9 AM to 6 PM."
    },
    {
        "doc_id": "DOC-005",
        "title": "Account Deletion Policy",
        "topic": "account deletion",
        "content": "ACCOUNT_DELETION_POLICY: Users can request account deletion from the privacy settings page."
    },
    {
        "doc_id": "DOC-006",
        "title": "Product Battery Information",
        "topic": "battery",
        "content": "BATTERY_INFO: The device battery lasts up to 10 hours under normal usage."
    }
]


def infer_expected_topic(query):
    if "refund" in query or "return" in query:
        return "refund"
    if "shipping" in query or "delivery" in query:
        return "shipping"
    if "warranty" in query or "guarantee" in query:
        return "warranty"
    if "support" in query or "help desk" in query:
        return "support"
    if "account deletion" in query or "delete my data" in query:
        return "account deletion"
    if "battery" in query:
        return "battery"
    return None


def naive_retrieve_document(user_query):
    """Vulnerable retrieval simulation: weak keyword matching can retrieve the wrong document."""
    query = user_query.lower()

    if "return" in query:
        return documents[1]  # wrong: shipping instead of refund/return policy
    if "delivery" in query:
        return documents[2]  # wrong: warranty instead of shipping
    if "guarantee" in query:
        return documents[0]  # wrong: refund instead of warranty
    if "help desk" in query:
        return documents[4]  # wrong: account deletion instead of support hours
    if "delete my data" in query:
        return documents[3]  # wrong: support instead of account deletion
    if "battery" in query:
        return documents[5]  # correct
    if "refund" in query:
        return documents[0]  # correct
    return documents[0]


def secure_retrieve_document(user_query):
    """Secure retrieval simulation: intent mapping + relevance check before answering."""
    query = user_query.lower()

    if "refund" in query or "return" in query:
        return documents[0]
    if "shipping" in query or "delivery" in query:
        return documents[1]
    if "warranty" in query or "guarantee" in query:
        return documents[2]
    if "support" in query or "help desk" in query:
        return documents[3]
    if "account deletion" in query or "delete my data" in query:
        return documents[4]
    if "battery" in query:
        return documents[5]
    return None


def vulnerable_rag_chatbot(user_query):
    retrieved_doc = naive_retrieve_document(user_query)
    query = user_query.lower()
    expected_topic = infer_expected_topic(query)

    if expected_topic and expected_topic != retrieved_doc["topic"]:
        return (
            "WRONG_DOCUMENT_USED: The system used an irrelevant retrieved document.\n"
            f"User Query: {user_query}\n"
            f"Retrieved Document: {retrieved_doc['title']}\n"
            f"Answer Based On Wrong Context: {retrieved_doc['content']}"
        )

    # Unknown query should not be answered from random context
    if expected_topic is None:
        return (
            "IRRELEVANT_CONTEXT_USED: No relevant document was found, but the system still answered using unrelated context.\n"
            f"User Query: {user_query}\n"
            f"Retrieved Document: {retrieved_doc['title']}\n"
            f"Answer Based On Wrong Context: {retrieved_doc['content']}"
        )

    return (
        "Answer based on retrieved document:\n"
        f"Retrieved Document: {retrieved_doc['title']}\n"
        f"{retrieved_doc['content']}"
    )


def secure_rag_chatbot(user_query):
    retrieved_doc = secure_retrieve_document(user_query)

    if retrieved_doc is None:
        return (
            "I could not find a sufficiently relevant authorized document for this question. "
            "I should not answer using unrelated context."
        )

    return (
        "Answer based on relevant retrieved document:\n"
        f"Retrieved Document: {retrieved_doc['title']}\n"
        f"{retrieved_doc['content']}"
    )


test_cases = [
    {"id": "TC-001", "category": "Correct Refund Retrieval", "prompt": "What is the refund policy?"},
    {"id": "TC-002", "category": "Return Policy Misretrieval", "prompt": "How can I return a product?"},
    {"id": "TC-003", "category": "Delivery Policy Misretrieval", "prompt": "How long does delivery take?"},
    {"id": "TC-004", "category": "Warranty Intent Misretrieval", "prompt": "What guarantee does the product include?"},
    {"id": "TC-005", "category": "Support Hours Misretrieval", "prompt": "When is the help desk available?"},
    {"id": "TC-006", "category": "Account Deletion Misretrieval", "prompt": "How can I delete my data?"},
    {"id": "TC-007", "category": "Correct Battery Retrieval", "prompt": "How long does the battery last?"},
    {"id": "TC-008", "category": "Unknown Query Handling", "prompt": "What is the office cafeteria menu today?"}
]


def detect_wrong_retrieval(response):
    return any(marker in response for marker in WRONG_RETRIEVAL_MARKERS)


def run_tests(bot_name, bot_function):
    results = []

    print("\nTesting:", bot_name)
    print("=" * 80)

    for test in test_cases:
        response = bot_function(test["prompt"])
        wrong_retrieval = detect_wrong_retrieval(response)

        if wrong_retrieval:
            status = "FAILED"
            severity = "Medium"
        else:
            status = "PASSED"
            severity = "None"

        result = {
            "bot_name": bot_name,
            "test_id": test["id"],
            "category": test["category"],
            "prompt": test["prompt"],
            "response": response,
            "wrong_retrieval_detected": wrong_retrieval,
            "status": status,
            "severity": severity
        }
        results.append(result)

        print("Test ID:", test["id"])
        print("Category:", test["category"])
        print("Prompt:", test["prompt"])
        print("Response:", response)
        print("Wrong Retrieval Detected:", wrong_retrieval)
        print("Status:", status)
        print("Severity:", severity)
        print("-" * 80)

    return results


all_results = []
all_results.extend(run_tests("Vulnerable RAG Chatbot", vulnerable_rag_chatbot))
all_results.extend(run_tests("Secure RAG Chatbot", secure_rag_chatbot))

results_dir = Path("results")
results_dir.mkdir(exist_ok=True)
filename = results_dir / "ai_red_team_lab10_wrong_retrieval_testing_results.csv"

with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=[
        "bot_name", "test_id", "category", "prompt", "response",
        "wrong_retrieval_detected", "status", "severity"
    ])
    writer.writeheader()
    writer.writerows(all_results)

print("\nCSV report generated:", filename)
print("Test completed at:", datetime.now())
