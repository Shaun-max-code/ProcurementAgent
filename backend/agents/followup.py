from backend.database import get_connection

def generate_followup(brand, supplier):

    return f"""
Subject: Follow-Up Regarding Procurement Discussion

Dear {supplier},

Thank you for taking the time to discuss the procurement requirements for {brand}.

We would appreciate an update regarding the next steps and any pending quotations.

Looking forward to your response.

Best Regards,
Procurement Team
"""