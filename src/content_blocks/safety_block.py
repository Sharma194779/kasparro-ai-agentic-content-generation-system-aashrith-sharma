from src.models.product_model import ProductModel
from typing import Dict, List


class SafetyBlock:
    
    @staticmethod
    def generate(product: ProductModel) -> Dict[str, any]:
        side_effects_list = [
            effect.strip() for effect in product.side_effects.split(',')
        ]
        
        contraindications = []
        if "sensitive" in product.side_effects.lower():
            contraindications = [
                "Not recommended for extremely sensitive skin",
                "Avoid if allergic to Vitamin C",
                "Discontinue if severe irritation occurs"
            ]
        
        return {
            "reported_side_effects": side_effects_list,
            "severity": "Mild",
            "who_can_use": product.skin_type,
            "contraindications": contraindications,
            "allergy_warning": "Contains Vitamin C derivative and Hyaluronic Acid",
            "pregnancy_safety": "Consult dermatologist before use during pregnancy",
            "discontinue_if": [
                "Severe burning or redness occurs",
                "Allergic reaction develops",
                "Skin barrier damage appears"
            ]
        }
