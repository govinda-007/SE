from abc import ABC, abstractmethod
from typing import List, Optional
from search_charging_station.domain.value_objects.postal_code import PostalCode
from search_charging_station.infrastructure.charging_station_table import ChargingStationModel

class IChargingStationRepository(ABC):
    @abstractmethod
    def find_by_postal_code(self, postal_code: PostalCode) -> List[ChargingStationModel]:
        """Retrieve all charging stations for a given postal code."""
        pass