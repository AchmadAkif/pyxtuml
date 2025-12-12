import os
from main import getAllClassInstances, getInstanceAttributes, getAllInstanceOperations, getInstanceStates
from jinja2 import Environment, FileSystemLoader

output_dir = 'gen'
os.makedirs(output_dir, exist_ok=True)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))
class_template = env.get_template('class.py.jinja2')
operations_template = env.get_template('operations.py.jinja2')
states_template = env.get_template('states.py.jinja2')

def render_operations(operations):
    if not operations:
        return ""
    return operations_template.render(operations=operations)

def render_states(states):
    if not states:
        return ''
    return states_template.render(states=states)

def render_class(kind: str):
    classes = getAllClassInstances(kind)
    
    for c in classes:
        className = c.Name.replace(' ', '')
        attributes = getInstanceAttributes(kind, lambda sel: sel.Key_Lett == c.Key_Lett)
        operations = getAllInstanceOperations(kind, lambda sel: sel.Key_Lett == c.Key_Lett)
        states = getInstanceStates(kind, lambda sel: sel.Key_Lett == c.Key_Lett)

        if states:
            states_content = render_states(states)
        else:
            states_content = ''

        operations_content = render_operations(operations)

        output = class_template.render(name=className, attributes=attributes, states_content=states_content, operations_content=operations_content)

        file_path = os.path.join(output_dir, f'{c.Name}.py')
        with open(file_path, 'w') as f:
            f.write(output)


render_class('O_OBJ')