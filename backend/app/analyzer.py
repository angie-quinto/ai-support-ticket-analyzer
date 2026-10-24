from models import TicketAnalysis

def analyze_ticket(ticket_details: str) -> TicketAnalysis:

    if not isinstance(ticket_details, str) or not ticket_details.strip():
        raise ValueError("Ticket data cannot be empty.")
    details = ticket_details.lower()


    if any(keyword in details for keyword in ["crash", "error", "bug", "issue"]):
        category = "bug"
    elif any(keyword in details for keyword in ["feature", "enhancement", "request"]):
        category = "feature"
    elif any(keyword in details for keyword in ["question", "inquiry"]):
        category = "question"
    elif any(keyword in details for keyword in ["payment", "billing", "invoice", "subscription", "charge", "refund"]):
        category = "billing"
    elif any(keyword in details for keyword in ["login", "authentication", "password"]):
        category = "account"
    else:
        category = "other"

    urgent_words = ["urgent", "immediately", "asap", "critical", "high priority"]
    if any(word in details for word in urgent_words):
        priority = "high"
    elif any(word in details for word in ["issue", "problem", "failed"]):
        priority = "medium"
    else:
        priority = "low"

    negative_words = [
        "angry", "frustrated", "terrible", "failed", "cannot",
        "charged twice", "broken",
    ]

    positive_words = ["thank you", "great", "excellent", "happy"]

    if any(word in details for word in negative_words):
        sentiment = "negative"
    elif any(word in details for word in positive_words):
        sentiment = "positive"
    else:
        sentiment = "neutral"

    return TicketAnalysis(
        category=category,
        priority=priority ,
        sentiment=sentiment,
        summary=f"Customer reports: {ticket_details.strip()[:250]}",
        suggested_next_step="Investigate the issue and follow up with the customer."
    )