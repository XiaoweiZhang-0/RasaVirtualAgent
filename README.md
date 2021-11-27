# rasa virtual agent

## This is repository for Aresty Research Project
## Instruction to run
```
Software version:

***the newest version of rasa seems to have bugs, please use the version I specified here instead**

rasa: 2.8.6

Python: 3.8.11

Instruction to run:

1.execute rasaOSserver.py and wait till the server is up

2.execute Devs/rasaAPI.py

```

## What I have done so far
```

1.Trained a nlu module that could interact with user following strictly the story graph

2.Wrote custom api to return rasa's response and parsed intent to voice-recognition module
```
## Problems
```
1. Response consists two or more intents
   Possible solution:
   parse sentence by sentence within one response
   if for intent1 == intent2:
   take them as one
   else:
   treat intent by intent
2. For one sentence, there may be two ways of intepreting it
   for example: you are late may 1.gives an intention for asking excuse 2.blame someone for lateness
```
