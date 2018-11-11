from automaton.builder.XmlBuilder import getClassFromElement, getclass, setPropertyOnObject


class Context():
    def __init__(self):
        self.mapping = {}
        pass


class XmlContextBuilder():
    def __init__(self):
        pass

    def parseActionArgsMapping(self, read_only_context, state_name, action_name, root_node):
        mapping = {
            'args': {},
            'args_from_context': []
        }

        context_nodes = root_node.findall('context-property')
        for contextElement in context_nodes:
            context_prop_name = contextElement.attrib['name']
            mapping['args_from_context'].append(context_prop_name)

        action_base_nodes = root_node.findall('param')
        for actionArgElement in action_base_nodes:
            arg_name = actionArgElement.attrib['name']
            arg_value = actionArgElement.text
            mapping['args'][arg_name] = arg_value

        return mapping

    def parseActionResultMapping(self, read_only_context, state_name, action_name, root_node):
        return {}

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
                
                action_args_root_node = mapElement.find('args')
                if action_args_root_node is not None:
                    handler.mapping[state_name][action_name]['args_mapping'] = \
                        self.parseActionArgsMapping(handler, state_name, action_name, action_args_root_node)

                action_results_root_node = mapElement.find('results')
                if action_results_root_node is not None:
                    handler.mapping[state_name][action_name]['result_mapping'] = \
                        self.parseActionResultMapping(handler, state_name, action_name, action_args_root_node)



        return handler
