# rasa virtual agent

## Project description
```
This is the nlu module of ECA project, which aims to build a virtual reality training platform for teachers. Teachers will interact with virtual intelligent agents simulating all kinds of scenarios they may encounter at work. The aim of ECA project is to systematically study the impact of embodied conversational agents on learning outcomes of teachers in high poverty schools, where rates of disruptive behaviors are three times national estimates and where teacher stress and turnover is empirically linked to disruptive behaviors.
```
## Instruction to run
#### the newest version of rasa seems to have bugs, please use the version I specified here instead
```
Software version:

rasa: 2.8.6

Python: 3.8.11

Instruction to run:

1.execute rasaOSserver.py and wait till the server is up

2.execute Devs/rasaAPI.py

```

## What I have done so far
```

1.Developed the nlu module with rasa open-source machine learning framework, and write custom api, which can return rasa’s response and parsed intent, to incorporate with a speech recognition and text-to-speech module to serve as the soul of the agent.

2.Constructed the sample story and its interaction tree graph. This is the blueprint in early stage of the project to test the robustness of the agent.
3.Read relevant papers in CASA,IEEE AIVR, IEEE VR and SCA to find the entry point for publishing new paper.

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
