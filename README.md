# SD_Framework

System Dynamics Python Framework
This framework allows the building and simulation of System Dynamic Models. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This Framework uses the Python 2D library [matplotlib](https://matplotlib.org) 

### Usage

Below a step-by-step tutorial on how to create a System-Dynamik Model using this framework.

#1. Create all system variables
``` 
# create a constant with a inital value
constant = Constant.Constant('constantName', 'constantUnit', 300)

# create a level with a inital value
level = Level.Level('levelName', 'levelUnit', 500)

# create a auxiliary
auxiliary = Auxiliary.Auxiliary('auxiliaryName', 'auxiliaryUnit')
```

#2. Create all flows
```
# create a flow 
flow = Flow.Flow('flowName', 'flowUnit')
```

#3. Create the model
```
# create a model, set starttime, endtime and timesteps
model = Model.Model("modelName", 0, 100, 1)
# add all system variables and flows to the model
model.addSystemVariable(constant)
model.addSystemVariable(level)
model.addSystemVariable(auxiliary)
model.addSystemVariable(flow)
```

