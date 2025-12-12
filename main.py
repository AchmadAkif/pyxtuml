from bridgepoint import ooaofooa
from xtuml import navigate_one as one
from xtuml import navigate_many as many

m = ooaofooa.load_metamodel('Tracking.xtuml')

## GET ALL CLASS INSTANCES FROM METAMODEL
def getAllClassInstances(kind: str): 
	classInstancesList = m.select_many(kind)
	
	return classInstancesList 
 
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

	return statesList

## GET INSTANCE STATE TRANSITIONS
def getInstanceStateTransitions(kind: str, args):
	statesList = getInstanceStates(kind, args)
	transitionsList = many(statesList).SM_TXN[506]()

	return transitionsList 
    

WoSesh = m.select_one('O_OBJ', lambda sel: sel.name == 'WorkoutSession')
for o_tfr in many(WoSesh).O_TFR[115]():
	print(o_tfr.Action_Semantics_internal)
