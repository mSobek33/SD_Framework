# System Dynamic Framework - Python
This framework allows the building and simulation of System Dynamic Models. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This Framework uses the Python 2D library [matplotlib](https://matplotlib.org) 

### Usage

Below a step-by-step tutorial on how to create a System-Dynamik Model using this framework.

#### 1. Create all system variables
``` 
# create a constant with a inital value
constant = Constant.Constant('constantName', 'constantUnit', 300)

# create a level with a inital value
level = Level.Level('levelName', 'levelUnit', 500)

# create a auxiliary
auxiliary = Auxiliary.Auxiliary('auxiliaryName', 'auxiliaryUnit')
```

#### 2. Create all flows
```
# create a flow 
flow = Flow.Flow('flowName', 'flowUnit')
flow2 = Flow.Flow('flow2Name', 'flow2Unit')
```


#### 3. Define input- and outputflows for level
```
level.addInputFlow(flow)
level.addOutputFlow(flow2)
```

#### 4. Create the model
```
# create a model, set starttime, endtime and timesteps
model = Model.Model("modelName", 0, 100, 1)
# add all system variables and flows to the model
model.addSystemVariable(constant)
model.addSystemVariable(level)
model.addSystemVariable(auxiliary)
model.addSystemVariable(flow)
# ...
```

#### 5. Define the causal edges in the model
```
model.defineCausalEdge(auxiliary, level)
```


#### 6. Define and add equations to variables
```
# create equation, pass all systemVariables as parameters 
flowEquation = Equation("equationName", auxiliary, constant)
# define calculation rule
flowEquation.defineFunctionByLambda( lambda : auxiliary.currentValue * constant.currentValue)
# add equation to systemVariable
flow.addEquation(flowEquation)

# ...

# create equation, pass all systemVariables as parameters 
levelEquation = Equation("levelEquationName", flow, flow2)
# define calculation rule
levelEquation.defineFunction("flowName - flowName2")
# add equation to systemVariable
level.addEquation(levelEquation)
```

#### 7. Starting the model calculation
```
model.run()
```

 #### 8. Display and print results
 ```
 # create a ResultVisualizatior
 result = ResultVisualization()
 # write results in an CSV
 result.createCSV(model, 'output.csv')
 # display result diagramms
 result.drawGraphic(model)
 ```
