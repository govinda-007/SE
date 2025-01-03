from sqlalchemy import Column, Integer, String, Float
from search_charging_station.infrastructure.database import SessionLocal, engine, Base

class ChargingStationModel(Base):
    __tablename__ = "charging_stations"

    station_id = Column(String, primary_key=True, index=True)
    postal_code = Column(String, index=True)
    latitude = Column(String)
    longitude = Column(String)
    location=Column(String)
    street = Column(String)
    district = Column(String)
    federal_state = Column(String)
    operator = Column(String)
    power_charging_dev = Column(Integer)
    commission_date = Column(String)
    type_charging_device=Column(String)
    cs_status=Column(String)
