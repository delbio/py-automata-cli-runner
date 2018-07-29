# Py Automata Cli Runner

Run from cli an automaton described by xml file

## How to install

```
basher install delbio/py-automata-cli-runner
```

## How to use

Create a model of Automaton like this into file **automaton.model.xml**:

```
<?xml version="1.0" encoding="UTF-8" ?>
<Automaton module="automaton.core.Automaton" name="Automaton">
    <States>
        <State module="automaton.placeholder" name="PlaceHolderState" type="BEGIN" >
            <Property name="stateName">Begin</Property>
        </State>
        <State module="automaton.placeholder" name="PlaceHolderState" type="-" >
            <Property name="stateName">StateA</Property>
        </State>
        <State module="automaton.placeholder" name="PlaceHolderState" type="END" >
            <Property name="stateName">End</Property>
        </State>
    </States>
    <Actions>
        <Action module="automaton.placeholder" name="PlaceHolderAction" source="Begin" target="StateA">
            <Property name="actionName">Start</Property>
        </Action>
        <Action module="automaton.placeholder" name="PlaceHolderAction" source="StateA" target="StateA">
            <Property name="actionName">StayHere</Property>
        </Action>
        <Action module="automaton.placeholder" name="PlaceHolderAction" source="StateA" target="End">
            <Property name="actionName">GoToEnd</Property>
        </Action>
    </Actions>
</Automaton>
```

then exec:

```
py-automata-cli-runner run automaton.model.xml
```

Runner run automata automatically, if more then one action if present for current state, runner ask to user to select action.

## Requirements

- bash 3.5
- python3

## Refs:

- https://github.com/delbio/py-automata
- https://github.com/delbio/py-automata-extras
