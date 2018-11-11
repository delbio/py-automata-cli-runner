import sys
import argparse
import os

from defusedxml.ElementTree import parse

from automaton.builder.XmlBuilder import XmlBuilder
from Runner import Runner
from ErrorHandler import ErrorHandlerXmlBuilder
from ActionSelector import NextActionSelectorXmlBuilder
from Context import XmlContextBuilder


def allow_local_module_if_requested(filepath, element):
    try:
        # if local-module-enabled is not present
        # parse raise exception
        element.attrib['local-module-enabled']
        # local-module-enabled present, skip value
        # Allow Modules that are in config file folder
        absConfigFilePath = os.path.abspath(filepath)
        absConfigDirPath = os.path.dirname(absConfigFilePath)
        sys.path.append(absConfigDirPath)
        print("Local Module enabled\n")
    except KeyError:
        print("No local modules enabled.\n")
    pass


def build_from_xml(filepath):
    builder = XmlBuilder()
    root = parse(filepath).getroot()
    allow_local_module_if_requested(filepath, root)
    automaton = builder.newObjectFromXmlElement(root)
    error_handler_builder = ErrorHandlerXmlBuilder()
    error_handler = error_handler_builder.newObjectFromXmlElement(root)
    next_action_selector_builder = NextActionSelectorXmlBuilder()
    next_action_selector = next_action_selector_builder.newObjectFromXmlElement(root)
    context_builder = XmlContextBuilder()
    context = context_builder.newObjectFromXmlElement(root)
    return {
        'automaton': automaton,
        'error_handler': error_handler,
        'next_action_selector': next_action_selector,
        'context': context,
    }


def getArgs():
    parser = argparse.ArgumentParser(description='CLI Automaton Runner')
    parser.add_argument('config', help='config file path')
    parser.add_argument('-i', dest='interactive',
                        action='store_const', const=True, default=False,
                        help='run automaton into interactive mode'
                        )
    return parser.parse_args()


if __name__ == "__main__":
    args = getArgs()
    components = build_from_xml(args.config)
    components['interactive'] = args.interactive
    runner = Runner()
    runner.run(**components)
