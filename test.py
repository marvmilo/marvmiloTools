import marvmiloTools as mm
import pandas as pd
import sys

mm.timer.start()
sp = mm.ScriptPrint("TEST", block = False, log = True)
print = sp.print

d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar", "dict": {"hello": "world"}}]}
l = [1, {'a': 2}, ["hi", {'foo': "bar"}]]
df = pd.DataFrame({1: [10], 2: [20]})
string = "hello world"
number = 10.7

settings = mm.json.load("test.json")
settings_copy = settings.copy()
settings_copy.test = "hello world"

print(settings)
print(settings_copy)

print(mm.get_variable_name(df, locals()))
print(mm.__version__)

mm.json.save(settings, "test_save.json")
sp.finish()