from src.models.product_model import ProductModel
from typing import Dict


class AnswerBlock:
    
    QUESTION_TEMPLATES = {
        "ingredient": "This product contains {ingredients}",
        "benefit": "The main benefit is {benefit}",
        "usage": "Apply {usage} as directed",
        "safety": "Side effects may include {side_effects}",
        "price": "This product is priced at {price}",
        "skin_type": "This product is designed for {skin_type} skin"
    }
    
    @staticmethod
    def generate(question: str, product: ProductModel) -> Dict[str, any]:
        
        question_lower = question.lower()
        
        if any(word in question_lower for word in ["contain", "ingredient", "formula"]):
            answer = f"This product contains {', '.join(product.key_ingredients)} as key active ingredients"
            category = "Ingredient"
        
        elif any(word in question_lower for word in ["benefit", "work", "effect", "result"]):
            answer = f"The main benefits are {' and '.join(product.benefits)}"
            category = "Benefits"
        
        elif any(word in question_lower for word in ["use", "apply", "how to", "application"]):
            answer = f"Usage instructions: {product.how_to_use}"
            category = "Usage"
        
        elif any(word in question_lower for word in ["side effect", "risk", "safe", "allergic"]):
            answer = f"Possible side effects: {product.side_effects}"
            category = "Safety"
        
        elif any(word in question_lower for word in ["price", "cost", "afford"]):
            answer = f"The product is priced at {product.price}"
            category = "Pricing"
        
        elif any(word in question_lower for word in ["skin type", "suitable", "oily", "combination"]):
            answer = f"This product is suitable for {', '.join(product.skin_type)} skin types"
            category = "Skin Type Compatibility"
        
        else:
            answer = f"{product.name} is a premium skincare product with {', '.join(product.benefits)} benefits"
            category = "General Information"
        
        return {
            "question": question,
            "answer": answer,
            "category": category,
            "confidence": 0.95,
            "source": "Product Data"
        }
