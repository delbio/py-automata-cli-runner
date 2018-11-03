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
