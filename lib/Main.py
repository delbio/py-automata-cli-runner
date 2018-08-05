import sys
import argparse

from defusedxml.ElementTree import parse

from automaton.builder.XmlBuilder import XmlBuilder
from automaton.runner.Runner import SimpleRunner

# Allow use python Modules that are located into script execution folder
# es:
# $ cd automaton_flow_folder
# # all module that are in this folder can be used into automaton.xml
# $ cli-runner run automaton.xml
sys.path.append('./')


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
