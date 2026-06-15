def generate_email(
    email_type,
    supplier,
    product
):

    if email_type == "OUTREACH":

        return f"""
Subject: Manufacturing Opportunity

Hello {supplier},

We are currently sourcing a manufacturing partner for:

Product: {product}

Could you let us know if you can support this opportunity?

Please respond:

YES - We can do it
NO - We cannot do it
MAYBE - Need more information

Regards,
Aekovera AI
"""

    elif email_type == "YES":

        return f"""
Subject: Next Steps

Hello {supplier},

Amazing.

We are excited to hear that you can support this project.

Do you currently support referral commissions for sourcing partners?

We would love to discuss additional opportunities.

Regards,
Aekovera AI
"""

    elif email_type == "NO":

        return f"""
Subject: Future Opportunities

Hello {supplier},

Thank you for your response.

Could you please complete our supplier capability form so we can match future opportunities more accurately?

Regards,
Aekovera AI
"""

    elif email_type == "MAYBE":

        return f"""
Subject: Additional Information

Hello {supplier},

Thank you for reviewing the opportunity.

Could you let us know exactly what additional information you need?

We will collect the requirements and get back to you.

Regards,
Aekovera AI
"""

    elif email_type == "FOLLOWUP":

        return f"""
Subject: Follow Up

Hello {supplier},

Just checking in regarding the manufacturing opportunity.

Please let us know if you are still interested.

Regards,
Aekovera AI
"""

    elif email_type == "ESCALATION":

        return f"""
Subject: Human Assistance Required

Hello Team,

This supplier requires human review.

Supplier: {supplier}

Please investigate and determine next steps.

Regards,
Aekovera AI
"""

    return "Invalid Email Type"