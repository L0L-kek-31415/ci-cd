from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder

from app.database import SessionLocal
from app.model import Job
from app.schema import JobSchema as Job_schema


app = FastAPI()


def get_db():
    db_session_local = SessionLocal()
    try:
        yield db_session_local
    finally:
        db_session_local.close()


@app.get("/", response_model=List[Job_schema])
def root(db_session: Session = Depends(get_db)):
    jobs = jsonable_encoder(db_session.query(Job).all())
    return JSONResponse(content=jobs)


@app.post("/create/", response_model=Job_schema)
def create_job(job: Job_schema, db_session: Session = Depends(get_db)):
    new_job = Job(title=job.title,
                  company=job.company,
                  is_active=job.is_active)
    print(new_job, "new_job\n", job)
    db_session.add(new_job)
    db_session.commit()
    db_session.refresh(new_job)
    return new_job


@app.get("/hc/")
def healthcheck():
    return Response(status_code=200)
