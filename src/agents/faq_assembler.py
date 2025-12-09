from typing import Dict, Any, List
from src.models.product_model import ProductModel
from src.content_blocks import AnswerBlock


class FAQAssemblerAgent:
    
    def __init__(self):
        self.name = "FAQAssemblerAgent"
        self.responsibility = "Assemble FAQ page using questions and answer blocks"
    
    def process(
        self,
        product: ProductModel,
        questions: List[Dict[str, str]]
    ) -> Dict[str, Any]:
        
        faqs = []
        
        for q_item in questions[:5]:
            question = q_item['question']
            category = q_item['category']
            
            answer_data = AnswerBlock.generate(question, product)
            
            faq_entry = {
                "id": f"faq_{len(faqs) + 1}",
                "question": question,
                "answer": answer_data['answer'],
                "category": category,
                "helpful": False,
                "views": 0
            }
            faqs.append(faq_entry)
        
        faq_page = {
            "page_type": "FAQ Page",
            "product_name": product.name,
            "total_faqs": len(faqs),
            "categories": list(set([q['category'] for q in questions])),
            "faqs": faqs,
            "metadata": {
                "page_generated": True,
                "generation_method": "Agentic Assembly",
                "blocks_used": ["AnswerBlock"],
                "questions_total": len(questions),
                "faqs_selected": len(faqs)
            }
        }
        
        return faq_page
