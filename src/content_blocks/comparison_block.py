from src.models.product_model import ProductModel
from typing import Dict, List


class ComparisonBlock:
    
    @staticmethod
    def generate(
        product_a: ProductModel,
        product_b: ProductModel
    ) -> Dict[str, any]:
        
        def extract_price_value(price_str: str) -> float:
            try:
                return float(price_str.replace('₹', '').strip())
            except ValueError:
                return 0
        
        price_a = extract_price_value(product_a.price)
        price_b = extract_price_value(product_b.price)
        
        return {
            "product_a": {
                "name": product_a.name,
                "concentration": product_a.concentration,
                "key_ingredients": product_a.key_ingredients,
                "benefits": product_a.benefits,
                "price": product_a.price,
                "side_effects": product_a.side_effects
            },
            "product_b": {
                "name": product_b.name,
                "concentration": product_b.concentration,
                "key_ingredients": product_b.key_ingredients,
                "benefits": product_b.benefits,
                "price": product_b.price,
                "side_effects": product_b.side_effects
            },
            "comparison_metrics": {
                "ingredient_overlap": len(
                    set(product_a.key_ingredients) & set(product_b.key_ingredients)
                ),
                "total_unique_ingredients": len(
                    set(product_a.key_ingredients) | set(product_b.key_ingredients)
                ),
                "price_difference": abs(price_a - price_b),
                "more_affordable": product_a.name if price_a < price_b else product_b.name
            },
            "recommendation": f"{product_a.name} is suitable for {', '.join(product_a.skin_type)} skin types"
        }
