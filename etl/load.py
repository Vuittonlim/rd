from sqlalchemy import create_engine
from dotenv import load_dotenv
from transform import transform
import os

# Load .env file
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Establish engine
engine = create_engine(DATABASE_URL, echo=True)
conn = engine.connect()

# Create table in postgresql and insert rows
df = transform()
df.to_sql('station_volumes', engine, if_exists='replace', index=False)
