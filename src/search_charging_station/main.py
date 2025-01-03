import sys
import os

# Ensure the 'src' directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'src')))
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker
from search_charging_station.infrastructure.database import engine, Base, SessionLocal
from search_charging_station.infrastructure.repositories.charging_station_repository import ChargingStationRepository
from search_charging_station.domain.services.charging_station_service import ChargingStationService

# Create all tables in the database
Base.metadata.create_all(bind=engine)

def main():
    # Start a session
    DATABASE_URL = "sqlite:///infrastructure/tables/berlincharginghub.db"
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    db_session = Session()
    
    # Initialize the repository with the session
    repository = ChargingStationRepository(db_session)
    
    # Initialize the service with the repository
    service = ChargingStationService(repository)
    
    # Use the service to fetch data
    postal_code = "Berlin"  # Example postal code
    stations = service.find_stations_by_postal_code(postal_code)
    print(stations)

    # Close the session after usage
    db_session.close()

if __name__ == "__main__":
    main()
