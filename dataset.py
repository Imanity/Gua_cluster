import numpy as np

class Data:
    def __init__(self, val, key, allkeys):
        self.val = np.array(val)
        self.key = key
        self.cluster = 0
        self.allkeys = allkeys

class Dataset:
    def __init__(self):
        self.data = []
        self.keys = []
        self.fields = []
    
    # Read from CSV file
    def readFromFile(self, filename, val_field, key_field):
        val_area = []
        key_area = 0
        with open(filename, 'r') as f:
            lines = f.readlines()
            self.fields = lines[0].split(',')
            for i in range(0, len(self.fields)):
                if self.fields[i] in val_field:
                    val_area.append(i)
                if self.fields[i] == key_field:
                    key_area = i
            
            for i in range(1, len(lines)):
                vals = lines[i].split(',')
                val = []
                for val_id in val_area:
                    val.append(eval(vals[val_id]))
                key = vals[key_area]
                if key not in self.keys:
                    self.keys.append(key)
                allkeys = vals[key_area:]
                self.data.append(Data(val, key, allkeys))
    
    # Write to CSV file
    def writeToFile(self, filename):
        f = open(filename, 'w')
        for i in range(0, len(self.fields)):
            if i >= len(self.data[0].val) and i < 22:
                continue
            f.write(self.fields[i])
            if i < len(self.fields) - 1:
                f.write(',')
        f.write('')
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data[i].val)):
                f.write(str(self.data[i].val[j]))
                f.write(',')
            for j in range(0, len(self.data[i].allkeys)):
                f.write(str(self.data[i].allkeys[j]))
                if j < len(self.data[i].allkeys) - 1:
                    f.write(',')
            f.write('')
