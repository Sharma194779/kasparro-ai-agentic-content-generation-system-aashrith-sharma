from typing import Dict, Any
from src.models.product_model import ProductModel
from src.content_blocks import (
    BenefitsBlock, UsageBlock, SafetyBlock,
    IngredientsBlock, PricingBlock
)


class ProductPageAssemblerAgent:
    
    def __init__(self):
        self.name = "ProductPageAssemblerAgent"
        self.responsibility = "Assemble product page using content blocks and template"
    
    def process(self, product: ProductModel) -> Dict[str, Any]:
        
        benefits_data = BenefitsBlock.generate(product)
        usage_data = UsageBlock.generate(product)
        safety_data = SafetyBlock.generate(product)
        ingredients_data = IngredientsBlock.generate(product)
        pricing_data = PricingBlock.generate(product)
        
        product_page = {
            "page_type": "Product Page",
            "product": {
                "name": product.name,
                "type": product.product_type.value,
                "concentration": product.concentration
            },
            "overview": {
                "title": f"{product.name} - Premium Vitamin C Serum",
                "description": f"{product.name} is a high-potency skincare serum designed for {', '.join(product.skin_type)} skin types. With {product.concentration} Vitamin C concentration, it delivers professional-grade results for brightening and anti-aging.",
                "skin_types": product.skin_type
            },
            "benefits": benefits_data,
            "ingredients": ingredients_data,
            "usage": usage_data,
            "safety": safety_data,
            "pricing": pricing_data,
            "metadata": {
                "page_generated": True,
                "generation_method": "Agentic Assembly",
                "blocks_used": [
                    "BenefitsBlock",
                    "IngredientsBlock",
                    "UsageBlock",
                    "SafetyBlock",
                    "PricingBlock"
                ]
            }
        }
        
        return product_page
