import pandas as pd
from search_charging_station.infrastructure.charging_station_table import ChargingStationModel
from search_charging_station.infrastructure.database import SessionLocal, engine, Base
import uuid
import re
import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

def import_charging_stations_from_csv(file_path: str):
    # Load CSV file
    df = pd.read_csv(file_path, delimiter=';', low_memory=False)

    # Ensure the column names match the database schema
    column_mapping = {
        "Postleitzahl": "postal_code",
        "Breitengrad": "latitude",
        "Längengrad": "longitude",
        "Ort": "location",
        "Straße": "street",
        "Kreis/kreisfreie Stadt": "district",
        "Bundesland": "federal_state",
        "Betreiber": "operator",
        "Nennleistung Ladeeinrichtung [kW]": "power_charging_dev",
        "Art der Ladeeinrichung": "type_charging_device",
        "Inbetriebnahmedatum": "commission_date"
    }

    # Rename columns according to the mapping
    df = df.rename(columns=column_mapping)

    # Initialize the database session
    session = SessionLocal()

    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)

    # Insert data into the database
    for _, row in df.iterrows():
        # Generate a unique station_id if it's not in the CSV
        station_id = str(uuid.uuid4())

            
        # Create the charging station object with the generated station_id
        charging_station = ChargingStationModel(
            station_id=station_id,
            postal_code=row["postal_code"],
            latitude=row["latitude"],
            longitude=row["longitude"],
            street=row["street"],
            district=row["district"],
            location=row["location"],
            federal_state=row["federal_state"],
            operator=row["operator"],
            power_charging_dev=row["power_charging_dev"],
            type_charging_device=row["type_charging_device"],
            commission_date=row["commission_date"],
            cs_status="Available"  # Default status
        )

        # Add and commit the data
        session.add(charging_station)

    session.commit()
    session.close()

    print("Data successfully imported!")

if __name__ == "__main__":
    import_charging_stations_from_csv("../shared/infrastructre/datasets/Ladesaeulenregister.csv")
