import random


def select_action_from_list(nextInputs, interactive):
    if not interactive and len(nextInputs) == 1:
        return nextInputs[0]

    actionName = input('User must select an action: ' + ', '.join(list(nextInputs)) + ' : ')
    try:
        i = int(actionName)
        if 0 <= i < len(list(nextInputs)):
            return nextInputs[i]
        else:
            print('\tSelect a number from 0 to ', len(list(nextInputs)) - 1)
            return select_action_from_list(nextInputs, interactive)
    except ValueError as e:
        pass

    if actionName in nextInputs:
        return actionName

    return select_action_from_list(nextInputs, interactive)


class ExecutionResult:
    def __init__(self):
        self.automaton = None
        pass

    def startExecution(self):
        print('Start from:\t', self.automaton.getCurrentState())
        pass

    def nextCurrentState(self, state):
        print('Current State:\t', state)
        pass

    def doAction(self, actionName):
        print('Exec Action: ', actionName)
        pass

    def stopExecution(self):
        print('Stopped into:\t', self.automaton.getCurrentState())
        pass


class NextActionSelector:
    def __init__(self):
        pass

    def nextAction(self, state, interactive):
        nextInputs = state.getNextInputs()
        print("\tNext inputs:\t" + ', '.join(list(nextInputs)))
        return select_action_from_list(nextInputs, interactive)


class ActionExecutionErrorHandler:
    def __init__(self):
        self.mapping = {}
        pass

    def handleError(self, state, actionName, error):
        state_handlers = self.mapping.get(state.getName(), None)
        if state_handlers is None:
            raise error
        next_action = state_handlers.get(error.__class__.__name__, None)
        if next_action is None:
            raise error

        return next_action




class Runner:
    def __init__(self):
        self.interactive = False
        self.nextActionSelector = None
        self.errorHandler = None
        pass

    def execAction(self, automaton, actionName, result):
        try:
            result.doAction(actionName)
            automaton.doAction(actionName)
            automaton.move(actionName)
            result.nextCurrentState(automaton.getCurrentState())
        except Exception as e:
            if self.errorHandler is None:
                raise e
            self.execAction(
                automaton,
                self.errorHandler.handleError(automaton.getCurrentState(), actionName, e),
                result,
            )
        pass

    def run(self, automaton):
        result = ExecutionResult()
        setattr(result, 'automaton', automaton)
        result.startExecution()
        try:
            while not automaton.isFinished():
                actionName = self.nextActionSelector.nextAction(automaton.getCurrentState(), self.interactive)
                self.execAction(automaton, actionName, result)
        finally:
            result.stopExecution()
