from typing import Dict, Any
from src.models.product_model import ProductModel
from src.content_blocks import ComparisonBlock


class ComparisonAssemblerAgent:
    
    def __init__(self):
        self.name = "ComparisonAssemblerAgent"
        self.responsibility = "Assemble comparison page between two products"
    
    def process(
        self,
        product_a: ProductModel,
        product_b: ProductModel
    ) -> Dict[str, Any]:
        
        comparison_data = ComparisonBlock.generate(product_a, product_b)
        
        comparison_page = {
            "page_type": "Comparison Page",
            "comparison_title": f"{product_a.name} vs {product_b.name}",
            "timestamp": "2024-12-10",
            "products": {
                "product_a": {
                    "name": product_a.name,
                    "concentration": product_a.concentration,
                    "skin_type": product_a.skin_type,
                    "price": product_a.price,
                    "benefits": product_a.benefits,
                    "ingredients": product_a.key_ingredients,
                    "side_effects": product_a.side_effects
                },
                "product_b": {
                    "name": product_b.name,
                    "concentration": product_b.concentration,
                    "skin_type": product_b.skin_type,
                    "price": product_b.price,
                    "benefits": product_b.benefits,
                    "ingredients": product_b.key_ingredients,
                    "side_effects": product_b.side_effects
                }
            },
            "comparison_analysis": {
                "ingredient_overlap": comparison_data['comparison_metrics']['ingredient_overlap'],
                "total_unique_ingredients": comparison_data['comparison_metrics']['total_unique_ingredients'],
                "price_difference": str(comparison_data['comparison_metrics']['price_difference']),
                "more_affordable": comparison_data['comparison_metrics']['more_affordable'],
                "recommendation": comparison_data['recommendation']
            },
            "detailed_comparison": comparison_data,
            "metadata": {
                "page_generated": True,
                "generation_method": "Agentic Assembly",
                "blocks_used": ["ComparisonBlock"]
            }
        }
        
        return comparison_page
