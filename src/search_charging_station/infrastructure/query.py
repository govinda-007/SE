from database import SessionLocal,engine
from charging_station_table import ChargingStationModel

# Create a new database session
session = SessionLocal()

try:
    # Query all charging stations
    charging_stations = session.query(ChargingStationModel).all()
    # Print results
    for station in charging_stations:
        print(station.location)
finally:
    # Close the session
    session.close()


