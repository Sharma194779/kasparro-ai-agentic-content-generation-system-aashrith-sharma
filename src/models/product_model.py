from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum


class ProductType(Enum):
    SKINCARE = "skincare"
    BEAUTY = "beauty"
    WELLNESS = "wellness"


@dataclass
class ProductModel:
    name: str
    concentration: str
    skin_type: List[str]
    key_ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: str
    price: str
    product_type: ProductType = ProductType.SKINCARE
    
    def validate(self) -> bool:
        if not self.name or len(self.name.strip()) == 0:
            raise ValueError("Product name is required")
        if not self.price or len(self.price.strip()) == 0:
            raise ValueError("Price is required")
        if not self.key_ingredients or len(self.key_ingredients) == 0:
            raise ValueError("At least one ingredient is required")
        if not self.benefits or len(self.benefits) == 0:
            raise ValueError("At least one benefit is required")
        return True
    
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "concentration": self.concentration,
            "skin_type": self.skin_type,
            "key_ingredients": self.key_ingredients,
            "benefits": self.benefits,
            "how_to_use": self.how_to_use,
            "side_effects": self.side_effects,
            "price": self.price,
            "product_type": self.product_type.value
        }
