from typing import Dict, Any, List, Callable
from src.models.product_model import ProductModel


class DAGNode:
    
    def __init__(
        self,
        name: str,
        agent,
        dependencies: List[str] = None
    ):
        self.name = name
        self.agent = agent
        self.dependencies = dependencies or []
        self.completed = False
        self.result = None


class DAGExecutor:
    
    def __init__(self):
        self.nodes = {}
        self.execution_order = []
    
    def add_node(
        self,
        name: str,
        agent,
        dependencies: List[str] = None
    ):
        node = DAGNode(name, agent, dependencies)
        self.nodes[name] = node
    
    def execute(self, initial_data: Dict[str, Any]) -> Dict[str, Any]:
        self._topological_sort()
        
        results = {}
        results['initial_data'] = initial_data
        
        print("AGENTIC CONTENT GENERATION PIPELINE EXECUTION")
        print("=" * 70)
        
        for node_name in self.execution_order:
            node = self.nodes[node_name]
            
            print(f"\n[STAGE {len([n for n in self.execution_order[:self.execution_order.index(node_name) + 1] if self.nodes[n].dependencies])}] {node.name}")
            
            dependencies_results = {
                dep: results.get(dep) for dep in node.dependencies
            }
            
            if node.dependencies:
                node.result = node.agent.process(
                    initial_data,
                    **dependencies_results
                )
            else:
                if node_name == 'data_parser':
                    node.result = node.agent.process(initial_data)
                elif node_name == 'question_generator':
                    node.result = node.agent.process(results['data_parser']['product_a'])
                elif node_name == 'product_page_assembler':
                    node.result = node.agent.process(results['data_parser']['product_a'])
                elif node_name == 'comparison_assembler':
                    node.result = node.agent.process(
                        results['data_parser']['product_a'],
                        results['data_parser']['product_b']
                    )
                elif node_name == 'faq_assembler':
                    node.result = node.agent.process(
                        results['data_parser']['product_a'],
                        results['question_generator']
                    )
                elif node_name == 'validation_agent':
                    node.result = node.agent.process(
                        results['faq_assembler'],
                        results['product_page_assembler'],
                        results['comparison_assembler']
                    )
            
            node.completed = True
            results[node_name] = node.result
            
            print(f"COMPLETED: {node.name}")
        
        return results
    
    def _topological_sort(self):
        visited = set()
        stack = []
        
        def visit(name: str):
            if name in visited:
                return
            visited.add(name)
            
            node = self.nodes[name]
            for dep in node.dependencies:
                visit(dep)
            
            stack.append(name)
        
        for name in self.nodes:
            visit(name)
        
        self.execution_order = stack
