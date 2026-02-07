from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///leadscore.db")

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    company = Column(String)
    company_size = Column(Integer)
    industry = Column(String)
    role = Column(String)
    source = Column(String)
    pages_viewed = Column(Integer)
    time_on_site = Column(Float)
    opened_email = Column(Integer)   
    clicked_email = Column(Integer)  
    last_contacted = Column(DateTime)
    converted = Column(Integer)      

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    lead_id = Column(Integer, ForeignKey("leads.id"))
    predicted_prob = Column(Float)
    model_version = Column(String)
    created_at = Column(DateTime)

class ModelRegistry(Base):
    __tablename__ = "model_registry"
    model_version = Column(String, primary_key=True)
    metrics_json = Column(JSON)
    model_path = Column(String)
    trained_at = Column(DateTime)
def init_db():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    init_db()
    print("Database and tables created successfully!")
