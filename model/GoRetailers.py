from dataclasses import dataclass


@dataclass
class GoRetailers:
    retailer_code : int
    retailer_name : str
    type: str
    country: str

    def __eq__(self, other):
        return self.retailer_code == other.retailer_code

    def __hash__(self):
        return hash(self.retailer_code)

    def __str__(self):
        return f"{self.retailer_name} ({self.retailer_code})- {self.type} {self.country}"
