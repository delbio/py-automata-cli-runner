from automaton.builder.XmlBuilder import getClassFromElement, getclass, setPropertyOnObject


class ActionExecutionErrorHandler:
    def __init__(self):
        self.mapping = {}
        pass

    def getErrorName(self, error):
        return error.__class__.__name__

    def handleError(self, state, actionName, error):
        state_name = state.getName()
        state_handlers = self.mapping.get(state_name, None)
        if state_handlers is None:
            raise error

        error_name = self.getErrorName(error)
        next_action = state_handlers.get(error_name, None)
        if next_action is None:
            raise error

        return next_action


class ErrorHandlerXmlBuilder():
    def __init__(self):
        pass

    def newObjectFromXmlElement(self, element):
        root_node = element.find('Error')
        # handler = getClassFromElement(element)()
        handler = ActionExecutionErrorHandler()
        if root_node is None:
            return handler

        setPropertyOnObject('Property', root_node, handler)

        state_nodes = root_node.findall('States/State')
        for stateElement in state_nodes:
            state_name = stateElement.attrib['name']
            handler.mapping[state_name] = {}

            errorHandlerOnStateNodes = stateElement.findall('Handler')
            for mapElement in errorHandlerOnStateNodes:
                error_class = mapElement.attrib['error']
                action_name = mapElement.attrib['action']
                handler.mapping[state_name][error_class] = action_name

        return handler
