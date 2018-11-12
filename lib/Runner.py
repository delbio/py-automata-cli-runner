class ExecutionResult:
    def __init__(self, automaton, error_handler, next_action_selector, context, interactive):
        self.automaton = automaton
        self.interactive = interactive
        self.context = context
        pass

    def startExecution(self):
        print('Start from:\t', self.automaton.getCurrentState())
        pass

    def nextCurrentState(self, state):
        print('Current State:\t', state)
        pass

    def doAction(self, action_name, args):
        print('Exec Action: ', action_name, ' with args: ', args)
        pass

    def stopExecution(self):
        print('Stopped into:\t', self.automaton.getCurrentState())
        pass


class Runner:
    def __init__(self):
        pass

    def exec_action(self, automaton, action_name, result, error_handler, next_action_selector, context):
        try:
            args = context.get_action_args(automaton.getCurrentState(), action_name)
            result.doAction(action_name, args)
            automaton.doAction(action_name, **args)
            automaton.move(action_name)
            result.nextCurrentState(automaton.getCurrentState())
        except Exception as e:
            if error_handler is None:
                raise e
            self.exec_action(
                automaton,
                error_handler.handleError(automaton.getCurrentState(), action_name, e),
                result,
                error_handler,
                next_action_selector,
                context
            )
        pass

    def run(self, automaton, error_handler, next_action_selector, context, interactive):
        result = ExecutionResult(
            automaton, error_handler, next_action_selector, context, interactive
        )
        result.startExecution()
        try:
            while not automaton.isFinished():
                action_name = next_action_selector.nextAction(automaton.getCurrentState(), interactive)
                self.exec_action(
                    automaton,
                    action_name,
                    result,
                    error_handler,
                    next_action_selector,
                    context
                )
        finally:
            result.stopExecution()
