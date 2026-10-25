import pytest
from pydantic import ValidationError

from backend.app.analyzer import analyze_ticket
from backend.app.models import TicketAnalysis


def test_analyze_billing_ticket_details():
    ticket_details = "I was charged twice for my subscription. Please refund the extra charge."
    analysis = analyze_ticket(ticket_details)
    assert analysis.category == "billing"
    assert analysis.priority == "low"
    assert analysis.sentiment == "negative"
    assert analysis.summary.startswith("Customer reports:")
    assert analysis.suggested_next_step == "Investigate the issue and follow up with the customer."

def test_reject_empty_ticket_details():
    with pytest.raises(ValueError):
        analyze_ticket("")

def test_reject_whitespace_ticket_details():
    with pytest.raises(ValueError):
        analyze_ticket("   ")

def test_invalid_ticket_category():
    with pytest.raises(ValidationError):
        TicketAnalysis(
            category="invalid_category",
            priority="low",
            sentiment="negative",
            summary="This is a test summary.",
            suggested_next_step="This is a test next step."
        )

def test_analyze_account_ticket_details():
    ticket_details = "I cannot log in to my account. Please help me reset my password."
    analysis = analyze_ticket(ticket_details)
    assert analysis.category == "account"
    assert analysis.priority == "low"
    assert analysis.sentiment == "negative"
    assert analysis.summary.startswith("Customer reports:")
    assert analysis.suggested_next_step == "Investigate the issue and follow up with the customer."

