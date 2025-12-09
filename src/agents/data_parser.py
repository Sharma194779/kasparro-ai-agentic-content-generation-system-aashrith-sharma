from typing import Dict, Any
from src.models.product_model import ProductModel, ProductType


class DataParserAgent:
    
    def __init__(self):
        self.name = "DataParserAgent"
        self.responsibility = "Parse and validate product data into internal model"
    
    def process(self, raw_data: Dict[str, Any]) -> ProductModel:
        try:
            product = ProductModel(
                name=raw_data.get('name', ''),
                concentration=raw_data.get('concentration', ''),
                skin_type=raw_data.get('skin_type', []),
                key_ingredients=raw_data.get('key_ingredients', []),
                benefits=raw_data.get('benefits', []),
                how_to_use=raw_data.get('how_to_use', ''),
                side_effects=raw_data.get('side_effects', ''),
                price=raw_data.get('price', ''),
                product_type=ProductType.SKINCARE
            )
            
            product.validate()
            
            return product
        
        except ValueError as e:
            raise ValueError(f"Data parsing failed: {str(e)}")
        except Exception as e:
            raise Exception(f"Unexpected error in data parsing: {str(e)}")
