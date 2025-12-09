from typing import List, Dict
from src.models.product_model import ProductModel


class QuestionGeneratorAgent:
    
    def __init__(self):
        self.name = "QuestionGeneratorAgent"
        self.responsibility = "Generate categorized user questions from product data"
        self.categories = {
            "Informational": [],
            "Safety": [],
            "Usage": [],
            "Purchase": [],
            "Comparison": [],
            "Ingredients": []
        }
    
    def process(self, product: ProductModel) -> List[Dict[str, str]]:
        questions = []
        
        questions.extend(self._generate_informational(product))
        questions.extend(self._generate_safety(product))
        questions.extend(self._generate_usage(product))
        questions.extend(self._generate_purchase(product))
        questions.extend(self._generate_comparison(product))
        questions.extend(self._generate_ingredients(product))
        
        return questions
    
    def _generate_informational(self, product: ProductModel) -> List[Dict[str, str]]:
        return [
            {"question": f"What is {product.name}?", "category": "Informational"},
            {"question": f"What are the main benefits of {product.name}?", "category": "Informational"},
            {"question": f"Is {product.name} effective for skincare?", "category": "Informational"},
            {"question": f"How long does {product.name} take to show results?", "category": "Informational"}
        ]
    
    def _generate_safety(self, product: ProductModel) -> List[Dict[str, str]]:
        return [
            {"question": f"Is {product.name} safe to use?", "category": "Safety"},
            {"question": f"What are the side effects of {product.name}?", "category": "Safety"},
            {"question": f"Can I use {product.name} if I have sensitive skin?", "category": "Safety"},
            {"question": f"Are there any allergies associated with {product.name}?", "category": "Safety"}
        ]
    
    def _generate_usage(self, product: ProductModel) -> List[Dict[str, str]]:
        return [
            {"question": f"How should I use {product.name}?", "category": "Usage"},
            {"question": f"How many drops of {product.name} should I use?", "category": "Usage"},
            {"question": f"When should I apply {product.name}?", "category": "Usage"},
            {"question": f"Can I use {product.name} with other products?", "category": "Usage"}
        ]
    
    def _generate_purchase(self, product: ProductModel) -> List[Dict[str, str]]:
        return [
            {"question": f"What is the price of {product.name}?", "category": "Purchase"},
            {"question": f"Where can I buy {product.name}?", "category": "Purchase"},
            {"question": f"Is {product.name} worth the price?", "category": "Purchase"},
            {"question": f"Does {product.name} come with a warranty?", "category": "Purchase"}
        ]
    
    def _generate_comparison(self, product: ProductModel) -> List[Dict[str, str]]:
        return [
            {"question": f"How does {product.name} compare to other serums?", "category": "Comparison"},
            {"question": f"What makes {product.name} different?", "category": "Comparison"}
        ]
    
    def _generate_ingredients(self, product: ProductModel) -> List[Dict[str, str]]:
        return [
            {"question": f"What are the ingredients in {product.name}?", "category": "Ingredients"},
            {"question": f"What is the concentration of Vitamin C in {product.name}?", "category": "Ingredients"}
        ]
