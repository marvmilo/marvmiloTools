import marvmiloTools as mm

mm.timer.start()

print = mm.ScriptPrint("TEST").print

d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar", "dict": {"hello": "world"}}]}
l = [1, {'a': 2}, ["hi", {'foo': "bar"}]]
string = "hello world"
number = 10.7

settings = mm.json.load("test.json", object = False)
print(settings)

mm.json.save(settings, "test_save.json")

