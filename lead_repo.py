# from db import SessionLocal
# from db import Lead
# from sqlalchemy import select, update

# class LeadRepo:

#     def add_lead(data):
#         session = SessionLocal()

#         new_lead = Lead(
#             name = data['name'],
#             email = data['email'],
#             company = data['company'],
#             company_size = data['company_size'],
#             industry = data['industry'],
#             role = data['role'],
#             source = data['source'],
#             pages_viewed = data['pages_viewed'],
#             time_on_site = data['time_on_site'],
#             opened_email = data['opened_email'],  
#             clicked_email = data['clicked_email'], 
#             last_contacted = data['last_contacted'],
#             converted =    data['converted']
#         )

#         session.add(new_lead)

#         session.commit()

#         session.refresh(new_lead)

#         session.close()

#         return new_lead
    

#     def get_lead_by_id(lead_id):

#         with SessionLocal() as session:
#             lead = session.get(Lead, lead_id)

#             return lead



#     def list_leads():

#         with SessionLocal() as session:
#             stmt = select(Lead)

#             lead = session.scalars(stmt).all()

#             return lead
        

#     def update_lead(lead_id, updates):

#         with SessionLocal() as session:

#             lead = session.get(Lead, lead_id)

#             if lead:

#                 lead.converted = 




from sqlalchemy import text
from db import Lead, SessionLocal


class LeadRepo:

    def add_lead(data):

        with SessionLocal() as session:

            sql = text(""" INSERT INTO LEADS (name, email, company, company_size, industry, role, 
                                   source, pages_viewed, time_on_site, opened_email, 
                                   clicked_email, last_contacted, converted)
                       VALUES (:name, :email, :company, :company_size, :industry, :role, 
                                   :source, :pages_viewed, :time_on_site, :opened_email, 
                                   :clicked_email, :last_contacted, :converted)

                                    """)