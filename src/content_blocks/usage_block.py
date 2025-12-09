from src.models.product_model import ProductModel
from typing import Dict


class UsageBlock:
    
    @staticmethod
    def generate(product: ProductModel) -> Dict[str, any]:
        instructions = product.how_to_use.split('.')
        cleaned_instructions = [
            inst.strip() for inst in instructions
            if inst.strip()
        ]
        
        return {
            "application_instructions": product.how_to_use,
            "steps": cleaned_instructions,
            "frequency": "Once daily in morning routine",
            "precautions": [
                "Apply to clean, dry skin",
                "Follow with sunscreen",
                "Patch test before full application",
                "Avoid contact with eyes"
            ],
            "best_practices": [
                "Use 2-3 drops only",
                "Apply before heavier serums",
                "Store away from direct sunlight",
                "Discard 6 months after opening"
            ]
        }
