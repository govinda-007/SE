# src/charging/domain/value_objects/postal_code.py
from dataclasses import dataclass
import re

@dataclass(frozen=True)
class PostalCode:
    value: str

    def __post_init__(self):
        if not self.is_valid():
            raise ValueError(f"Invalid postal code: {self.value}")

    def is_valid(self) -> bool:
        #pattern=r'^(10|12|13|14)\d{3}$'
        pattern = r'^[A-Za-z]+$'
        return bool(re.match(pattern,self.value))
