def print_result(obj):
    def decorated(*args, **kwargs):
        print(obj.__name__)
        data = obj(*args, **kwargs)
        if isinstance(data, dict):
            for i in data:
                print(i, ' = ', data[i])
        elif isinstance(data, list):
            for i in data:
                print(i)
        else:
            print(data)
        return data
    return decorated