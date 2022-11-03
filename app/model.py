from sqlalchemy import Column, Integer, String, Boolean

from app.database import Base, engine


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)


Base.metadata.create_all(bind=engine)
