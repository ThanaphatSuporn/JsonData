import json

class DataJson():
    def __init__(self):
        pass
    def saveJson(self, filename: str, Str: str):
        with open(filename, 'w') as f:
            json.dump(json.loads(Str), f, indent=4)

    def loadJson(self, filename: str):
        with open(filename, 'r') as f:
            return json.load(f)
    
    def updateJson(self, filename: str, key: str, value: str):
        data = self.loadJson(filename)
        data[key] = value
        self.saveJson(filename, json.dumps(data))
    
    def key(self, key):
        return self.loadJson(key)
    
    def value(self, value):
        return self.loadJson(value)
    
    def deleteKey(self, filename: str, key: str):
        data = self.loadJson(filename)
        if key in data:
            del data[key]
        self.saveJson(filename, json.dumps(data))
    
    def deleteValue(self, filename: str, value: str):
        data = self.loadJson(filename)
        for k, v in list(data.items()):
            if v == value:
                del data[k]
        self.saveJson(filename, json.dumps(data))
    
    def updateValue(self, filename: str, old_value: str, new_value: str):
        data = self.loadJson(filename)
        for k, v in list(data.items()):
            if v == old_value:
                data[k] = new_value
        self.saveJson(filename, json.dumps(data))
    
    def findKey(self, filename: str, key: str):
        data = self.loadJson(filename)
        if key in data:
            return data[key]
        else:
            return None
    
    def findValue(self, filename: str, value: str):
        data = self.loadJson(filename)
        for k, v in data.items():
            if v == value:
                return k
        return None
    
    def countKey(self, filename: str, key: str):
        data = self.loadJson(filename)
        return data.count(key)
    
    def countValue(self, filename: str, value: str):
        data = self.loadJson(filename)
        return sum(v == value for v in data.values())
    
    def sortByKey(self, filename: str):
        data = self.loadJson(filename)
        sorted_data = dict(sorted(data.items()))
        self.saveJson(filename, json.dumps(sorted_data, indent=4))
    
    def sortByValue(self, filename: str):
        data = self.loadJson(filename)
        sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))
        self.saveJson(filename, json.dumps(sorted_data, indent=4))
    
    def searchKey(self, filename: str, key: str):
        data = self.loadJson(filename)
        results = [k for k, v in data.items() if key in k]
        return results
    
    def searchValue(self, filename: str, value: str):
        data = self.loadJson(filename)
        results = [k for k, v in data.items() if v == value]
        return results
    