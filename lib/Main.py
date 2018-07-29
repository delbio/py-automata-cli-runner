import sys
import argparse

from defusedxml.ElementTree import parse

from automaton.builder.XmlBuilder import XmlBuilder
from automaton.runner.Runner import SimpleRunner

sys.path.append('./actions')


def build_from_xml(filepath):
    builder = XmlBuilder()
    root = parse(filepath).getroot()
    automaton = builder.newObjectFromXmlElement(root)
    print('Loaded Automaton: \n', automaton.__str__())
    return automaton

def getConfigFilePathFromArgs():
    parser = argparse.ArgumentParser(description='CLI Automaton Runner')
    parser.add_argument('config', help='config file path')
    args = parser.parse_args()
    return args.config

if __name__ == "__main__":
    automaton =  build_from_xml(getConfigFilePathFromArgs())
    runner = SimpleRunner()
    runner.run(automaton)
