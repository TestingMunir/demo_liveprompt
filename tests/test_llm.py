import os

from deepeval import evaluate
from deepeval.metrics import FaithfulnessMetric, AnswerRelevancyMetric,ContextualRelevancyMetric,BiasMetric
from deepeval.test_case import LLMTestCase

# Sample data
original_conversation = """
Salesperson: Good morning, sir. Do you have a moment?
Manager: Good morning! Yes, come in. What’s on your mind?
Salesperson: I’ve been reviewing my sales numbers...
"""

model_summary = """
The salesperson approaches the manager to discuss a decline in sales. They identify inconsistent follow-ups and competition as key issues. The manager advises daily follow-ups and offers to help improve sales pitches through role-play.
"""

reference_summary = """
A salesperson discussed declining sales with their manager. They cited inconsistent follow-ups and competition. The manager suggested daily follow-ups and role-play training. They agreed to meet again next week to review progress.
"""

# Define the test case
test_case = LLMTestCase(
    input=original_conversation,
    actual_output=model_summary,
    expected_output=reference_summary,
    retrieval_context=[original_conversation]
)

# Choose evaluation metrics
metrics = [
    FaithfulnessMetric(),
    AnswerRelevancyMetric(),
    ContextualRelevancyMetric(),
    BiasMetric()
]
# Run evaluation
evaluate([test_case], metrics)


