from sqlalchemy import text
from db import Lead, SessionLocal

class LeadRepo:
     
    @staticmethod
    def add_lead(data):
        with SessionLocal() as session:
            sql = text(""" 
                INSERT INTO leads (name, email, company, company_size, industry, role, 
                                   source, pages_viewed, time_on_site, opened_email, 
                                   clicked_email, last_contacted, converted)
                VALUES (:name, :email, :company, :company_size, :industry, :role, 
                                   :source, :pages_viewed, :time_on_site, :opened_email, 
                                   :clicked_email, :last_contacted, :converted)
                RETURNING *;
            """)
            result = session.execute(sql, data)
            session.commit()
            return result.fetchone()
        
    @staticmethod
    def get_lead_by_id(lead_id):
        with SessionLocal() as session:
            sql = text("SELECT * FROM leads WHERE id = :id")
            result = session.execute(sql, {"id": lead_id})
            return result.fetchone()

    @staticmethod
    def list_leads():
        with SessionLocal() as session:
            sql = text("SELECT * FROM leads")
            result = session.execute(sql)
            return result.fetchall()
        
    @staticmethod
    def update_lead(lead_id, updates):
        with SessionLocal() as session:
            for column, value in updates.items():
                sql = text(f"UPDATE leads SET {column} = :val WHERE id = :id")
                session.execute(sql, {"val": value, "id": lead_id})

            session.commit()
            return True

    @staticmethod
    def delete_lead(lead_id):
        with SessionLocal() as session:
            sql = text("DELETE FROM leads WHERE id = :id")
            session.execute(sql, {'id': lead_id})

        session.commit()
        return True
    
