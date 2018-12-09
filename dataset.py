import numpy as np

class Data:
    def __init__(self, val, key):
        self.val = np.array(val)
        self.key = key
        self.cluster = 0

class Dataset:
    def __init__(self):
        self.data = []
        self.keys = []
    
    # Read from CSV file
    def readFromFile(self, filename, val_field, key_field):
        val_area = []
        key_area = 0
        with open(filename, 'r') as f:
            lines = f.readlines()
            fields = lines[0].split(',')
            for i in range(0, len(fields)):
                if fields[i] in val_field:
                    val_area.append(i)
                if fields[i] == key_field:
                    key_area = i
            
            for i in range(1, len(lines)):
                vals = lines[i].split(',')
                val = []
                for val_id in val_area:
                    val.append(eval(vals[val_id]))
                key = vals[key_area]
                if key not in self.keys:
                    self.keys.append(key)
                self.data.append(Data(val, key))
