def combine_json(j1: dict, j2: dict) -> dict:
    for j2_key in j2:
        if j2_key not in j1:
            j1[j2_key] = j2[j2_key]
        elif type(j2[j2_key]) == list and type(j1[j2_key]) == list:
            j1[j2_key] = list(set(j1[j2_key] + j2[j2_key]))
        elif type(j1[j2_key]) == dict or type(j2[j2_key]) == dict:
            j1[j2_key] = combine_json(j1[j2_key], j2[j2_key])
    return j1


if __name__ == '__main__':
    J1 = {
        "Key1": "val1",
        "Key2": {
            "nestedKey1": "nestedValue1",
            "keyWithListVal": [1, 2, 4]
        }
    }

    J2 = {
        "Key1": "val2",
        "Key2": {
            "key4": "val4",
            "keyWithListVal": [5, 2, 3]
        },
        "key3": "val3",
        "key4": "val4"
    }

    print(combine_json(J1, J2))