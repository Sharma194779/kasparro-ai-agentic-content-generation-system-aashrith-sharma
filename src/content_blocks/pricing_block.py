from src.models.product_model import ProductModel
from typing import Dict


class PricingBlock:
    
    @staticmethod
    def generate(product: ProductModel) -> Dict[str, any]:
        price_value = product.price.replace('₹', '').strip()
        
        try:
            price_num = float(price_value)
            ml_estimate = 30
            price_per_ml = price_num / ml_estimate
            
            if price_num < 500:
                tier = "Budget-Friendly"
            elif price_num < 1000:
                tier = "Mid-Range"
            else:
                tier = "Premium"
        except ValueError:
            price_per_ml = 0
            tier = "Standard"
        
        return {
            "mrp": product.price,
            "price_value": price_value,
            "currency": "INR",
            "price_tier": tier,
            "estimated_volume": "30ml",
            "price_per_ml": f"{price_per_ml:.2f}",
            "value_proposition": "Affordable luxury skincare",
            "comparison_note": "Competitive pricing for Vitamin C serum category"
        }
