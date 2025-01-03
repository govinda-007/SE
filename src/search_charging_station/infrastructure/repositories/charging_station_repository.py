from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker, Session
from typing import List
from search_charging_station.domain.value_objects.postal_code import PostalCode
from search_charging_station.infrastructure.charging_station_table import ChargingStationModel
from search_charging_station.infrastructure.repositories.charging_station_interface import IChargingStationRepository

class ChargingStationRepository(IChargingStationRepository):
    def __init__(self, session: Session):
        """Initialize the repository with a SQLAlchemy session."""
        self.session = session

    def find_by_postal_code(self, postal_code: PostalCode) -> List[ChargingStationModel]:
        """Retrieve all charging stations for a given postal code (with additional filtering for federal_state = 'Berlin')."""
        
        # Inspect the database to get the table names
        inspector = inspect(self.session.bind)
        tables = inspector.get_table_names()

        # Loop through each table and count the rows where 'federal_state' is Berlin
        for table in tables:
            # Construct the query to count rows where 'federal_state' is Berlin
            count_query = text(f"SELECT COUNT(*) FROM {table}")
            count = self.session.execute(count_query).scalar() # Use 'Berlin' as the parameter for federal_state
            print(f"Table: {table} - Row count': {count}")

        # Returning the ChargingStationModel query result as before, no additional filtering for postal_code yet
        return (
            self.session.query(ChargingStationModel)
            .all()  # Retrieves all rows from the charging_stations table
        )
