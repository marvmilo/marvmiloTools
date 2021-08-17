# marvmiloTools
**Version:** 1.6.0
# Description:
A tool a wrote for myself to have multiple functions and classes avalibale on diffrent servers and devices.
# HowTo:
## 1. Main
### 1.1 ScriptPrint:
Replace "print" function, where you can see in which script the print function was executed.
#### Example 1:
.  
├── first_script.py  
└── second_script.py 
first_script.py:
```
import marvmiloTools as mmt
print = mmt.ScriptPrint("MAIN").print

print("This is the FIRST script")

import second_script
```
second_script.py:
```
import marvmiloTools as mmt
print = mmt.ScriptPrint("IMPORTED").print

print("This is the SECOND script")
```
Execute like this:
```
~$ python first_script.py
```
Output:
```
[MAIN]: This is the FIRST script
[IMPORTED]: This is the SECOND script
``` 
&nbsp;  
Another feature is blocking the output, if running in background. So you don't ned space for logs with endless looping Scripts.
#### Example 2:  
```
print = mmt.ScriptPrint("NAME", block = True).print
```
&nbsp;   
### 1.2 Timer:
A build in timer for measuring runtimes.
#### Example:
```
import marvmiloTools as mmt
from time import sleep

#start the timer
mmt.timer.start()

sleep(3)

#pause timer
runtime = mmt.timer.pause()
print("Type of runtime: " + str(type(runtime)))
print("Runtime at pause: " + str(runtime))

#reset timer and get runtime function
mmt.timer.reset()
runtime = mmt.timer.get_runtime()
print("Runtime at reset: " + str(runtime))

#set some laps
mmt.timer.start()
for i in range(3):
    sleep(1)
    runtime = mmt.timer.set_lap()
    print("Runtime at lap " + str(i) + ": " + str(runtime))

#get all laps
laps = mmt.timer.get_laps()
print("Laps: " + str(laps))

sleep(2)

#get time of current lap without setting a lap
lap_runtime = mmt.timer.get_lap_runtime()
print("Current Lap Runtime: " + str(lap_runtime))
```
Output:
```
Type of runtime: <class 'datetime.timedelta'>
Runtime at pause: 0:00:03.003270
Runtime at reset: 0:00:00
Runtime at lap 0: 0:00:01.001151
Runtime at lap 1: 0:00:01.001191
Runtime at lap 2: 0:00:01.001231
Laps: [datetime.timedelta(seconds=1, microseconds=1151), datetime.timedelta(seconds=1, microseconds=1191), datetime.timedelta(seconds=1, microseconds=1231)]
Current Lap Runtime: 0:00:02.002030
```
&nbsp;  
### 1.3 get_variable_name
Converting variable in namespace into an string.
#### Example:
```
import marvmiloTools as mmt

#declare a variable
variable = "hello world"

#get name as string from variable
variable_name = mmt.get_variable_name(variable, locals())
print(variable_name, type(variable_name))
```
Output:
```
variable <class 'str'>
```
