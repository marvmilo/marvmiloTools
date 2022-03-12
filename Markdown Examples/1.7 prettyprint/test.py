import marvmiloTools as mmt

random_list = [1, 2, 3]
random_dict = {"a": "A", "b": "B"}
random_dictobj = mmt.dictionary.toObj(random_dict)

mmt.prettyprint(random_list)
mmt.prettyprint(random_dict)
mmt.prettyprint(random_dictobj)