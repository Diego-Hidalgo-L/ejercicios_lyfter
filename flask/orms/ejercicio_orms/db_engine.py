from sqlalchemy import create_engine

DB_URI = "postgresql://postgres:xyz0138@localhost:5432/postgres"
engine = create_engine(DB_URI) # echo=True

