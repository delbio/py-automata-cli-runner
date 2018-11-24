from automaton.builder.XmlBuilder import getClassFromElement, getclass, setPropertyOnObject


class Context():
    def __init__(self):
        self.mapping = {}
        self.context = {}
        pass

    def get_action_args(self, state, action_name):

        args = {}

        state_name = state.getName()
        state_handlers = self.mapping.get(state_name, None)
        if state_handlers is None:
            return args

        action_handlers = state_handlers.get(action_name, None)
        if action_handlers is None:
            return args

        mapping = action_handlers.get('args_mapping', None)
        if mapping is None:
            return args

        action_params = mapping.get('args', {})
        param_from_context_mapping = mapping.get('args_from_context', {})
        args = { **args, **action_params }

        for key in param_from_context_mapping:
            print('mapping: ', key, param_from_context_mapping, self.context)
            param_name = param_from_context_mapping.get(key, None)
            if param_name is None:
                raise ValueError('No param name founded into mapping for context prop: '+key)
            args[param_name] = self.context.get(key, None)

        return args

    def update(self, state, action_name, args, result):
        pass


class XmlContextBuilder():
    def __init__(self):
        pass

    def parseActionArgsMapping(self, read_only_context, state_name, action_name, root_node):
        mapping = {
            'args': {},
            'args_from_context': {}
        }

        context_nodes = root_node.findall('context')
        for contextElement in context_nodes:
            context_prop_name = contextElement.attrib['name']
            arg_name = contextElement.attrib['param']
            mapping['args_from_context'][context_prop_name] = arg_name

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
