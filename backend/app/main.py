from models import TicketAnalysis

ticket = TicketAnalysis (
    category="bug",
    priority="high",
    sentiment="negative",
    summary="The application crashes when I try to upload a file.",
    suggested_next_step="Please investigate the file upload functionality and fix the crash issue."
)


print(ticket.model_dump())