from typing import List
from search_charging_station.domain.value_objects.postal_code import PostalCode
from search_charging_station.infrastructure.repositories.charging_station_repository import ChargingStationRepository
from search_charging_station.domain.aggregates.charging_station import ChargingStation

class ChargingStationService:
    def __init__(self, repository: ChargingStationRepository):
        self.repository = repository

    def find_stations_by_postal_code(self, postal_code: PostalCode) -> List[ChargingStation]:
        """Find charging stations by postal code."""
        code = PostalCode(postal_code)
        return self.repository.find_by_postal_code(code)
