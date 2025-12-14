from bridgepoint import oal
import xtuml

class OALToPyWalker(xtuml.Walker):
	def __init__(self, model_var_name="model"):
		super().__init__()
		self.buffer = []
		self.indent_level = 0
		self.model_var = model_var_name
    
	def get_py_code(self):
		return "".join(self.buffer)
	
	def add_line(self, line):
		self.buffer.append("	" * self.indent_level + line + "\n")

	def increase_indent(self):
		self.indent_level += 1

	def decrease_indent(self):
		self.indent_level = max(0, self.indent_level - 1)

	def accept_IntegerNode(self, node):
		value = int(node.value)
		return value
	
	def accept_StringNode(self, node):
		value = node.value

		return value
	
	def accept_AssignmentNode(self, node):
		variable_access = self.accept(node.variable_access)
		expression = self.accept(node.expression)

	def accept_SelectedAccessNode(self, node, **kwargs):
		return kwargs['iteration_var']

	def accept_FieldAccessNode(self, node, **kwargs):
		handle_code = self.accept(node.handle, **kwargs)
		attr_name = node.name
		
		return f"{handle_code}.{attr_name}"
	
	def accept_BinaryOperationNode(self, node, **kwargs):
		operator = node.operator
		left_operand = self.accept(node.left, **kwargs)
		right_operand = self.accept(node.right)

		return f"{left_operand} {operator} {right_operand}"

	def accept_CreateObjectNode(self, node):
		var_name = node.variable_name
		key_letter = node.key_letter

		print(f"{var_name} = {key_letter}()")

	def accept_DeleteNode(self, node):
		var_name = node.variable_name

		print(f"del {var_name}")

	def accept_SelectFromNode(self, node):
		cardinality = node.cardinality
		var_name = node.variable_name
		key_letter = node.key_letter

		if cardinality == 'many':
			print(f"{var_name} = {key_letter}.instances")
		else:
			print(f"{var_name} = next(iter({key_letter}.instances), None)")

	def accept_SelectFromWhereNode(self, node):
		cardinality = node.cardinality
		var_name = node.variable_name
		key_letter = node.key_letter
		iteration_var = 'item'
		where = self.accept(node.where_clause, iteration_var=iteration_var)

		if cardinality == 'many':
			print(f"{var_name} = [{iteration_var} for {iteration_var} in {key_letter}.instances if {where}]")
		else:
			print(f"{var_name} = next(({iteration_var} for {iteration_var} in {key_letter}.instances if {where}), None)")

## TEST TRANSLATOR ##
oal_code = 'select any oven from instances of MO_O where selected.state == "Awaiting Cooking Request";'

ast = oal.parse(oal_code)
w = OALToPyWalker()
# w.visitors.append(xtuml.tools.NodePrintVisitor())
w.accept(ast)