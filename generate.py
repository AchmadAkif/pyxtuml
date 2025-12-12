import os
from main import getAllClassInstances, getInstanceAttributes, getAllInstanceOperations
from jinja2 import Environment, FileSystemLoader

output_dir = 'gen'
os.makedirs(output_dir, exist_ok=True)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('class.py.jinja2')

def accept_class(kind: str):
    classes = getAllClassInstances(kind)
    for c in classes:
        attributes = getInstanceAttributes(kind, lambda sel: sel.Key_Lett == c.Key_Lett)
        operations = getAllInstanceOperations(kind, lambda sel: sel.Key_Lett == c.Key_Lett)
        
        output = template.render(name=c.Name, attributes=attributes, operations=operations)
        
        file_path = os.path.join(output_dir, f'{c.Name}.py')
        with open(file_path, 'w') as f:
            f.write(output)

accept_class('O_OBJ')