import os
project_dir = os.path.abspath(os.path.join(os.getcwd(), 'tables'))
DATABASE_URL = "sqlite:///infrastructure/tables/berlincharginghub.db"
print(DATABASE_URL)

from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker

# Create an engine instance (replace DATABASE_URL with your actual database URL)
engine = create_engine(DATABASE_URL)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Inspect the database to get the table names
inspector = inspect(engine)
tables = inspector.get_table_names()

# Loop through each table and count the rows where 'federal_state' is Berlin
for table in tables:
    # Use SQLAlchemy's text() function to mark the raw SQL query
    # Make sure the column 'federal_state' or 'Bundesland' exists in your table
    count_query = text(f"SELECT COUNT(*) FROM {table} WHERE federal_state = :state")
    count = session.execute(count_query, {'state': 'Berlin'}).scalar()  # Pass 'Berlin' as the parameter for federal_state
    print(f"Table: {table} - Row count where federal_state is 'Berlin': {count}")

# Close the session
session.close()
