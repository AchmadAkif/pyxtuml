from bridgepoint import ooaofooa
from xtuml import navigate_one as one
from xtuml import navigate_many as many
from xtuml import navigate_subtype as subtype

m = ooaofooa.load_metamodel('Tracking.xtuml')

## GET ALL CLASS INSTANCES FROM METAMODEL
def getAllClassInstances(kind: str): 
	classInstancesList = m.select_many(kind)
	
	return classInstancesList 
 
## GET AN INSTANCE FROM METAMODEL
def getInstance(kind: str, args):
	classInstance = m.select_one(kind, args)

	return classInstance

## GET INSTANCE STATE MACHINE
def getInstanceStateMachine(kind: str, args):
	instance = m.select_one(kind, args)
	instanceSM = one(instance).SM_ISM[518]()
	stateMachine = one(instanceSM).SM_SM[517]()

	return stateMachine

## GET INSTANCE STATES
def getInstanceStates(kind: str, args):
	stateMachine = getInstanceStateMachine(kind, args)
	statesList = many(stateMachine).SM_STATE[501]()

	if len(statesList) == 0:
		return None

	return statesList

## GET INSTANCE STATE TRANSITIONS
def getInstanceStateTransitions(kind: str, args):
	statesList = getInstanceStates(kind, args)
	transitionsList = many(statesList).SM_TXN[506]()

	return transitionsList 
    
## GET INSTANCE ATTRIBUTES
def getInstanceAttributes(kind: str, args):
    instance = getInstance(kind, args)
    attributesList = many(instance).O_ATTR[102]()

    return attributesList

## GET ALL INSTANCE-BASED OPERATIONS
def getAllInstanceOperations(kind: str, args):
	instance = getInstance(kind, args)
	operationsList = many(instance).O_TFR[115]()    

	if not operationsList:
		return None
	
	return operationsList

# sm_sm = getInstanceStateMachine('O_OBJ', lambda sel: sel.name == 'Goal')
# statesList = many(sm_sm).SM_STATE[501]()

# for state in statesList:
# 	sm_txn = many(state).SM_TXN[506]()
# 	print(state.Name)

# 	for txn in sm_txn:
# 		print(f" SM_TXN {txn.Trans_ID}")

# 		tah = one(txn).SM_TAH[530]()
# 		ah = subtype(tah, 513)
# 		act = one(ah).SM_ACT[514]()
# 		print(act)



		




	
		
	