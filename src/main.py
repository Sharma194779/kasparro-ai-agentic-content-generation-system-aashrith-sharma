import json
import os
from src.agents import (
    DataParserAgent,
    QuestionGeneratorAgent,
    ProductPageAssemblerAgent,
    FAQAssemblerAgent,
    ComparisonAssemblerAgent,
    ValidationAgent
)
from src.models import ProductModel
from src.orchestration import DAGExecutor


def create_output_directory():
    if not os.path.exists('output'):
        os.makedirs('output')


def save_json(data: dict, filename: str):
    filepath = os.path.join('output', filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved: {filepath}")


def main():
    create_output_directory()
    
    print("INITIALIZING AGENTIC CONTENT GENERATION SYSTEM\n")
    
    product_data = {
        'name': 'GlowBoost Vitamin C Serum',
        'concentration': '10% Vitamin C',
        'skin_type': ['Oily', 'Combination'],
        'key_ingredients': ['Vitamin C', 'Hyaluronic Acid'],
        'benefits': ['Brightening', 'Fades dark spots'],
        'how_to_use': 'Apply 2-3 drops in the morning before sunscreen',
        'side_effects': 'Mild tingling for sensitive skin',
        'price': '699'
    }
    
    print("STAGE 1: PARSING PRODUCT DATA")
    print("-" * 70)
    
    data_parser = DataParserAgent()
    product_a = data_parser.process(product_data)
    
    print(f"Product Parsed: {product_a.name}")
    print(f"Ingredients: {', '.join(product_a.key_ingredients)}")
    print(f"Benefits: {', '.join(product_a.benefits)}")
    
    product_b_data = {
        'name': 'LuminaGlow Vitamin C+ Complex',
        'concentration': '12% Vitamin C',
        'skin_type': ['Normal', 'Oily'],
        'key_ingredients': ['Vitamin C', 'Ferulic Acid', 'Glycerin'],
        'benefits': ['Brightening', 'Anti-aging', 'Hydrating'],
        'how_to_use': 'Apply 3-4 drops morning and evening',
        'side_effects': 'Slight redness in first week',
        'price': '899'
    }
    
    product_b = data_parser.process(product_b_data)
    print(f"Fictional Product Created: {product_b.name}")
    
    print("\nSTAGE 2: GENERATING QUESTIONS")
    print("-" * 70)
    
    question_generator = QuestionGeneratorAgent()
    questions = question_generator.process(product_a)
    print(f"Generated {len(questions)} categorized questions")
    for q in questions[:3]:
        print(f"  - {q['question']} ({q['category']})")
    print(f"  ... and {len(questions) - 3} more")
    
    print("\nSTAGE 3: ASSEMBLING PRODUCT PAGE")
    print("-" * 70)
    
    product_assembler = ProductPageAssemblerAgent()
    product_page = product_assembler.process(product_a)
    print(f"Product Page assembled with {len(product_page)} sections")
    
    print("\nSTAGE 4: ASSEMBLING FAQ PAGE")
    print("-" * 70)
    
    faq_assembler = FAQAssemblerAgent()
    faq_page = faq_assembler.process(product_a, questions)
    print(f"FAQ Page assembled with {len(faq_page['faqs'])} Q&A pairs")
    
    print("\nSTAGE 5: ASSEMBLING COMPARISON PAGE")
    print("-" * 70)
    
    comparison_assembler = ComparisonAssemblerAgent()
    comparison_page = comparison_assembler.process(product_a, product_b)
    print(f"Comparison Page assembled: {product_a.name} vs {product_b.name}")
    
    print("\nSTAGE 6: VALIDATION")
    print("-" * 70)
    
    validator = ValidationAgent()
    validation_report = validator.process(faq_page, product_page, comparison_page)
    
    print(f"FAQ Page: {'VALID' if validation_report['pages']['faq_page']['is_valid'] else 'INVALID'}")
    print(f"Product Page: {'VALID' if validation_report['pages']['product_page']['is_valid'] else 'INVALID'}")
    print(f"Comparison Page: {'VALID' if validation_report['pages']['comparison_page']['is_valid'] else 'INVALID'}")
    print(f"Overall Status: {validation_report['overall_status']}")
    
    print("\nSTAGE 7: SAVING JSON OUTPUTS")
    print("-" * 70)
    
    save_json(faq_page, 'faq.json')
    save_json(product_page, 'product_page.json')
    save_json(comparison_page, 'comparison.json')
    save_json(validation_report, 'validation_report.json')
    
    print("\nPIPELINE EXECUTION COMPLETE")
    print("=" * 70)
    print(f"Output files saved to: output/")
    print(f"Files generated:")
    print(f"  - faq.json")
    print(f"  - product_page.json")
    print(f"  - comparison.json")
    print(f"  - validation_report.json")


if __name__ == "__main__":
    main()
