from src.models.product_model import ProductModel
from typing import Dict, List


class IngredientsBlock:
    
    INGREDIENT_INFO = {
        "Vitamin C": {
            "type": "Antioxidant",
            "concentration": "10%",
            "function": "Brightening, anti-aging, antioxidant protection"
        },
        "Hyaluronic Acid": {
            "type": "Humectant",
            "concentration": "Variable",
            "function": "Hydration, plumping, moisture retention"
        },
        "Ferulic Acid": {
            "type": "Antioxidant",
            "concentration": "0.5%",
            "function": "Stabilization, additional antioxidant benefits"
        },
        "Glycerin": {
            "type": "Humectant",
            "concentration": "Variable",
            "function": "Hydration, skin conditioning"
        }
    }
    
    @staticmethod
    def generate(product: ProductModel) -> Dict[str, any]:
        ingredients_detail = []
        
        for ingredient in product.key_ingredients:
            info = IngredientsBlock.INGREDIENT_INFO.get(
                ingredient,
                {
                    "type": "Active Ingredient",
                    "concentration": "Variable",
                    "function": f"Key active component"
                }
            )
            ingredients_detail.append({
                "name": ingredient,
                **info
            })
        
        return {
            "key_ingredients": product.key_ingredients,
            "detailed_ingredients": ingredients_detail,
            "total_ingredients": len(ingredients_detail),
            "main_active": product.key_ingredients[0] if product.key_ingredients else "N/A",
            "formulation_type": "Lightweight serum"
        }
