from automaton.builder.XmlBuilder import getClassFromElement, getclass, setPropertyOnObject


class Context():
    def __init__(self):
        pass


class XmlContextBuilder():
    def __init__(self):
        pass

    def newObjectFromXmlElement(self, element):
        root_node = element.find('Context')
        # handler = getClassFromElement(element)()
        handler = Context()
        if root_node is None:
            return handler
