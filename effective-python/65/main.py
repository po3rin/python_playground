import json

#:def try_finally_example(filename):
#     print("* Open file")
#     handle = open(filename, encoding="utf-8")
#     try:
#         print("reading data")
#         return handle.read()
#     finally:
#         print("calling close")
#         handle.close()

# filename = "random_data.txt"
# with open(filename, "wb") as f:
#     f.write(b'\xf1\xf2\xf3\xf4\xf5')

# data = try_finally_example(filename)


def load_json_key(data, key):
    try:
        print("aaa")
        result_dict = json.loads(data)
    except ValueError as e:
        print("bbb")
    else:
        print("ccc")
        return result_dict[key]


assert load_json_key('{"foo":"bar"}', "foo") == "bar"
