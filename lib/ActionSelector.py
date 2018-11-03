from automaton.builder.XmlBuilder import getClassFromElement, getclass, setPropertyOnObject


class NoInteractiveModeNoMappingForMultipleNextInputError(ValueError):
    def __init__(self):
        # Call the base class constructor with the parameters it needs
        super().__init__('Not interactive mode, mutliple action available, no mapping setted')


def select_action_from_list_recursive_interactive(nextInputs):
    actionName = input('User must select an action: ' + ', '.join(list(nextInputs)) + ' : ')
    try:
        i = int(actionName)
        if 0 <= i < len(list(nextInputs)):
            return nextInputs[i]
        else:
            print('\tSelect a number from 0 to ', len(list(nextInputs)) - 1)
            return select_action_from_list_recursive_interactive(nextInputs)
    except ValueError as e:
        pass

    if actionName in nextInputs:
        return actionName

    return select_action_from_list_recursive_interactive(nextInputs)


class NextActionSelector:
    def __init__(self):
        self.mapping = {}
        pass

    def nextAction(self, state, interactive):
        nextInputs = state.getNextInputs()
        print("\tNext inputs:\t" + ', '.join(list(nextInputs)))
        if not interactive and len(nextInputs) == 1:
            return nextInputs[0]

        if not interactive:
            print("\tMapping:\t", self.mapping)
            action_name = self.mapping.get(state.getName(), None)
            if action_name is None:
                raise NoInteractiveModeNoMappingForMultipleNextInputError()
            else:
                return action_name

        return select_action_from_list_recursive_interactive(nextInputs)


# Per le esecuzioni non interattive
# se e' presente piu' di una azione in uscita
# in un mapping deve essere definita la azione da usare

class NextActionSelectorXmlBuilder():
    def __init__(self):
        pass

    def newObjectFromXmlElement(self, element):
        root_node = element.find('ActionSelector')
        # handler = getClassFromElement(element)()
        handler = NextActionSelector()
        if root_node is None:
            return handler

        setPropertyOnObject('Property', root_node, handler)

        state_nodes = root_node.findall('States/State')
        for stateElement in state_nodes:
            state_name = stateElement.attrib['name']
            action_name = stateElement.text
            handler.mapping[state_name] = action_name

        return handler
