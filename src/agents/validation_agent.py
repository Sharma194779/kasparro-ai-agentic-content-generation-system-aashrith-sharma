import json
from typing import Dict, Any, List


class ValidationAgent:
    
    def __init__(self):
        self.name = "ValidationAgent"
        self.responsibility = "Validate JSON output correctness and completeness"
        self.validation_results = []
    
    def process(
        self,
        faq_page: Dict[str, Any],
        product_page: Dict[str, Any],
        comparison_page: Dict[str, Any]
    ) -> Dict[str, Any]:
        
        validation_report = {
            "validation_timestamp": "2024-12-10",
            "total_pages": 3,
            "pages": {}
        }
        
        validation_report['pages']['faq_page'] = self._validate_faq(faq_page)
        validation_report['pages']['product_page'] = self._validate_product(product_page)
        validation_report['pages']['comparison_page'] = self._validate_comparison(comparison_page)
        
        all_valid = all([
            validation_report['pages']['faq_page']['is_valid'],
            validation_report['pages']['product_page']['is_valid'],
            validation_report['pages']['comparison_page']['is_valid']
        ])
        
        validation_report['overall_status'] = "VALID" if all_valid else "INVALID"
        validation_report['total_errors'] = sum([
            len(validation_report['pages'][page]['errors'])
            for page in validation_report['pages']
        ])
        
        return validation_report
    
    def _validate_faq(self, faq_page: Dict[str, Any]) -> Dict[str, Any]:
        errors = []
        
        if 'page_type' not in faq_page:
            errors.append("Missing page_type field")
        
        if 'faqs' not in faq_page:
            errors.append("Missing faqs field")
        elif len(faq_page['faqs']) < 5:
            errors.append(f"FAQ count is {len(faq_page['faqs'])}, minimum 5 required")
        
        for idx, faq in enumerate(faq_page.get('faqs', [])):
            if 'question' not in faq:
                errors.append(f"FAQ {idx + 1}: Missing question field")
            if 'answer' not in faq:
                errors.append(f"FAQ {idx + 1}: Missing answer field")
        
        try:
            json.dumps(faq_page)
        except Exception as e:
            errors.append(f"Invalid JSON structure: {str(e)}")
        
        return {
            "page_name": "FAQ Page",
            "is_valid": len(errors) == 0,
            "errors": errors,
            "faq_count": len(faq_page.get('faqs', []))
        }
    
    def _validate_product(self, product_page: Dict[str, Any]) -> Dict[str, Any]:
        errors = []
        required_fields = ['page_type', 'product', 'benefits', 'ingredients', 'pricing']
        
        for field in required_fields:
            if field not in product_page:
                errors.append(f"Missing required field: {field}")
        
        try:
            json.dumps(product_page)
        except Exception as e:
            errors.append(f"Invalid JSON structure: {str(e)}")
        
        return {
            "page_name": "Product Page",
            "is_valid": len(errors) == 0,
            "errors": errors,
            "sections_present": len([k for k in product_page.keys() if k != 'metadata'])
        }
    
    def _validate_comparison(self, comparison_page: Dict[str, Any]) -> Dict[str, Any]:
        errors = []
        required_fields = ['page_type', 'products', 'comparison_analysis']
        
        for field in required_fields:
            if field not in comparison_page:
                errors.append(f"Missing required field: {field}")
        
        if 'products' in comparison_page:
            if 'product_a' not in comparison_page['products']:
                errors.append("Missing product_a in comparison")
            if 'product_b' not in comparison_page['products']:
                errors.append("Missing product_b in comparison")
        
        try:
            json.dumps(comparison_page)
        except Exception as e:
            errors.append(f"Invalid JSON structure: {str(e)}")
        
        return {
            "page_name": "Comparison Page",
            "is_valid": len(errors) == 0,
            "errors": errors,
            "products_compared": 2
        }
