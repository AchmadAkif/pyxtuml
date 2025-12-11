import os
from bridgepoint import ooaofooa
from xtuml import navigate_one as one
from xtuml import navigate_many as many

m = ooaofooa.load_metamodel('MicrowaveOven.xtuml')

## GET ALL CLASS INSTANCES FROM METAMODEL
# modelClassInstances = m.select_many('O_OBJ')

# for clazz in modelClassInstances:
# 	print(clazz.Name) 

## GET INSTANCE STATE
OvenInstance = m.select_one('O_OBJ', lambda sel: sel.name == 'Oven')
OvenInstanceSM = one(OvenInstance).SM_ISM[518]()
OvenSM = one(OvenInstanceSM).SM_SM[517]()
OvenStates = many(OvenSM).SM_STATE[501]()

for state in OvenStates:
	print(state.Name)
    

