from pydantic import BaseModel

class EmailPayload(BaseModel):
    email_id: str
    senderEmail: str
    body: str