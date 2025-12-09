from src.models.product_model import ProductModel
from typing import Dict, List


class BenefitsBlock:
    
    @staticmethod
    def generate(product: ProductModel) -> Dict[str, any]:
        benefits_with_descriptions = []
        
        benefit_descriptions = {
            "Brightening": "Makes skin appear brighter and more radiant",
            "Fades dark spots": "Reduces the appearance of hyperpigmentation and dark spots",
            "Anti-aging": "Helps reduce fine lines and wrinkles",
            "Hydrating": "Provides deep moisture to the skin",
            "Antioxidant": "Protects skin from environmental damage",
            "Smoothing": "Creates a smooth, even skin texture"
        }
        
        for benefit in product.benefits:
            description = benefit_descriptions.get(
                benefit,
                f"Provides {benefit.lower()} benefits"
            )
            benefits_with_descriptions.append({
                "benefit": benefit,
                "description": description
            })
        
        return {
            "primary_benefits": product.benefits,
            "detailed_benefits": benefits_with_descriptions,
            "concentration": product.concentration,
            "suitable_for": product.skin_type,
            "key_active": product.key_ingredients[0] if product.key_ingredients else "N/A"
        }
