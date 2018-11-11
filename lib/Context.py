from automaton.builder.XmlBuilder import getClassFromElement, getclass, setPropertyOnObject


class Context():
    def __init__(self):
        self.mapping = {}
        pass


class XmlContextBuilder():
    def __init__(self):
        pass

    def parseActionArgs(mapping, state, action_name, root_node):
        context_nodes = root_node.findall('context')
        for stateElement in context_nodes:
            handler.mapping[state_name][action_name] = {}


    def newObjectFromXmlElement(self, element):
        root_node = element.find('Context')
        # handler = getClassFromElement(element)()
        handler = Context()
        if root_node is None:
            return handler

        setPropertyOnObject('Property', root_node, handler)

        state_nodes = root_node.findall('States/State')
        for stateElement in state_nodes:
            state_name = stateElement.attrib['name']
            handler.mapping[state_name] = {}

            actionContextHandlerOnStateNodes = stateElement.findall('Actions/Action')
            for mapElement in actionContextHandlerOnStateNodes:
                action_name = mapElement.attrib['name']
                handler.mapping[state_name][action_name] = {}
                

                # parse context tag as action contex arg

                # parse arg tag as action arg

                # parse result tag as action result mapping to context

        return handler
