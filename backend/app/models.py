from typing import Literal
from pydantic import BaseModel, Field

class TicketAnalysis(BaseModel):
    category: Literal["bug", "billing", "account", "other"]
    priority: Literal["low", "medium", "high"]
    sentiment: Literal["positive", "neutral", "negative"]
    summary: str = Field(min_length=1, max_length=300)
    suggested_next_step: str = Field(min_length=1, max_length=300)