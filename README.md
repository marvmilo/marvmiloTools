# marvmiloTools
**Version:** 1.9.0

**Dependencies:**
- pandas
- dash
- dash-bootstrap-components
- paho-mqtt

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
&nbsp;  
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
Create a new instance of timer:
```
timer = mmt.Timer()
timer.start()
...
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
&nbsp;
### 1.4 random_ID
Creating a random ID of specific length.
#### Example:
```
import marvmiloTools as mmt
print(mmt.random_ID(10))
```
#### Output:
```
R1DBXY64KH73BPPF7WFT
```
&nbsp;
### 1.4 random_ID
CloudMQTT client with multiple functions.
#### Example:
```
import marvmiloTools as mmt

#init cloudMQTT client
cloudmqtt = mmt.CloudMQTT(
    client_name = "clientname", 
    channel = "channel", 
    qos = 0
)

#connect to server
cloudmqtt.connect(
    user = "user", 
    pw = "password", 
    addr = "cloudmqtt.com", 
    port = 1234
)

#reconnecting to server if no connection
if not cloudmqtt.check_connection():
    cloudmqtt.reconnect()

#on message function
def on_message(msg, topic):
    print(f"received message: '{msg}', topic: '{topic}'")
    
#binding on_message function to a topic
cloudmqtt.bind(topic = "hello", function = on_message)

#publishing a message
cloudmqtt.publish(topic = "hello", message = "world")

#response function
def on_request(msg, topic):
    resp = "hello world"
    print(f"publishing response: {resp}")
    return(resp)

#binding on_request to request topic
cloudmqtt.bind_response("demo", on_request)

#request data from server
resp = (
    cloudmqtt.request(
        topic = "demo",
        message = ".",
        retry = 5
    )
)
print("got response: " + resp)

#disconnecting form server
cloudmqtt.disconnect()
```
#### Output:
```
received message: 'world', topic: 'hello'
publishing response: hello world
got response: hello world
```
#### MQTT Messages:
![Messages](./Markdown%20Examples/1.5%20CloudMQTT/messages.png)
&nbsp;
## 2. Dash
### 2.1 flex_style
Dictionary for centering content in dash plotlys html.Div
#### Example:
```
import marvmiloTools as mmt
from dash import html

html.Div(
    children = [
        "hello world"
    ],
    style = mmt.dash.flex_style({
        "background-color": "black"
    })
)
```
&nbsp;
### 2.2 mobile_optimization
Meta tags for setting app to a mobile optiomized app.
#### Example:
```
import marvmiloTools as mmt
import dash

app = dash.Dash(__name__, meta_tags = [mmt.dash.mobile_optimization])
```
&nbsp;
### 2.3 content_div
For creating a dynamic scalealbe content Div.
#### Example:
```
import marvmiloTools as mmt
from dash import html
import dash_bootstrap_components as dbc

app.layout = html.Div(
    children = [
        dbc.Navbar(...),
        mmt.dash.content_div(
            width = "1000px",
            padding = "5%",
            content = [
                "content"
            ]
        )
    ]
)
```
&nbsp;
### 2.4 modal_header_close
Creating an modal header with close button and specific color.
#### Example:
```
import marvmiloTools as mmt
import dash_bootstrap_components as dbc

dbc.Modal(
    children = [
        mmt.dash.modal_header_close(
            title = "This is the header",
            close_id = "modal-close" #id of the close button,
            color = "#4287f5" #background color of header
        ),
        dbc.Modal_Body("This is modal body")
    ]
)
```
&nbsp;
### 2.5 random_ID
Creating random IDs compatible with dash.
#### Example:
```
import marvmiloTools as mmt
from dash import html

html.Div(
    children = "Hello World",
    id = mmt.dash.random_ID()
)
```
Output ID: 'MNPhNBfXcpVeHVVxuJeF' 
&nbsp;

&nbsp;
### 2.6 browsertime
Creating a Object in dash html form, wich provides the current clock time of the browser. That means the callbacks can calulate timezone of input.

Add this to your callbacks:
```
app.clientside_callback(*mmt.dash.browsertime.clientside_callback_args)
```

Add this in your html layout of the page: 
```
mmt.dash.browsertime.htmlObj()
```
Example Callback with browser time:
```
from dash.dependencies import Input, Output, State
import datetime as dt

@app.callback(
    [Output(...)],
    [Input(...)],
    [State("browser-time", "children")]
)
def callback(... , browsertime):
    time_shift_hours = dt.datetime.strptime(local_time, "%H:%M:%S").hour - dt.datetime.utcnow().hour
```
&nbsp;
### 2.6 nav
Simply creating a dash navbar with custom items.
```
import marvmiloTools as mmt

mmt.dash.nav.bar(
    logo = "url(/assets/logo.png)",
    logo_style = {
        "width": "3rem", 
        "height": "3rem",
        "background-size": "cover",
    },
    title = "Navbar Title",
    title_style = {
        "width": "15rem",
        "font-size": "1.5rem"
    }, 
    expand = "lg",
    items = [
        mmt.dash.nav.item.href(
            "Link",
            href = "https://github.com/marvmilo",
            target = "_blank",
            size = "lg"
        ),
        mmt.dash.nav.item.normal(
            "Button",
            id = "button-id",
            size = "lg"
        )
    ]
)
```

&nbsp;
## 3. Json
### 3.1 load
For opening and loading a json file to dictionary or marvmiloTools.DictObj
#### Example:
.  
├── example.json  
└── script.py  
&nbsp;  
example.json:
```
{
    "hello": "world"
}
```
script.py:
```
import marvmiloTools as mmt

dictionary = mmt.json.load("example.json", object=False)
DictObj = mmt.json.load("example.json")

print("Dictionary:")
print(dictionary)
print(type(dictionary))
print()
print("DictObject:")
print(DictObj)
print(type(DictObj))
```
Execute like this:
```
~$ python script.py
```
Output:
```
Dictionary:
{'hello': 'world'}
<class 'dict'>

DictObject:
{'hello': 'world'}
<class 'marvmiloTools.dictionary_tools.DictObject'>
``` 
&nbsp;  
### 3.2 save
For saving a dictionary or marvmiloTools.DictObject to a json file.
#### Example:
```
import marvmiloTools as mmt

dictionary = {"hello": "world"}
DictObj = mmt.dictionary.toObj(dictionary)

#save to json
mmt.json.save(dictionary, filename = "dictionary.json")
mmt.json.save(DictObj, filename = "DictObj.json")
```
Output as dictionary.json and DictObj.json:
```
{
    "hello": "world"
}
```
&nbsp;  
### 3.3 write
For writing a value directly to a json file without opening and saving.
#### Example:
.  
├── example.json  
└── script.py  
&nbsp;  
example.json:
```
{
    "dictionary": {
        "hello": "world"
    },
    "list": [
        "a",
        "b",
        "c"
    ]
}
```
script.py:
```
import marvmiloTools as mmt

mmt.json.write("value", "example.json", ["dictionary", "new"])
mmt.json.write("new", "example.json", ["list", 1])
```
Output example.json:
```
{
    "dictionary": {
        "hello": "world",
        "new": "value"
    },
    "list": [
        "a",
        "new",
        "b",
        "c"
    ]
}
```
&nbsp;  
## 4. Dictionary
### 4.1 toObj
Transforming to a dictionary to a marvmiloTools.DictObject. This Object can be used like a Class in Python
#### Example:
```
# pylint: disable = no-member
import marvmiloTools as mmt

dictionary = {"hello": "world", "list": ["string", 10, {"a": "b"}]}
#convert dictionary to Object
DictObj = mmt.dictionary.toObj(dictionary)

print(type(DictObj))
print(DictObj)
print(DictObj.hello)
print(DictObj.list[2].a)
```
(usining "# pylint: disable = no-member" with Visual Studio Code for disabeling "DictObj has no hello member" Error)  
&nbsp;  
Output:
```
<class 'marvmiloTools.dictionary_tools.DictObject'>
{'hello': 'world', 'list': ['string', 10, {'a': 'b'}]}
world
b
```
A DictObject has the same attributes and functions as a dictionary aswell
One extra function is pretty:
```
import marvmiloTools as mmt

DictObj = mmt.dictionary.toObj({"hello": "world"})
print(DictObj.pretty())
```
Output:
```
{
    "hello": "world"
}
```
&nbsp;  
### 4.2 toDict
Transforming a marvmiloTools.DictObject back to a standart dictionary.
#### Example:
```
import marvmiloTools as mmt

DictObj = mmt.dictionary.toObj({"hello": "world"})

#convert to dictionary
dictionary = mmt.dictionary.toDict(DictObj)
print(dictionary)
print(type(dictionary))
```
Output:
```
{'hello': 'world'}
<class 'dict'>
```
