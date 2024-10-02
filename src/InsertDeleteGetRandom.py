import random
class RandomizedSet:
    def __init__(self):
        self.values = {}
        self.arr = []


    def insert(self, val: int) -> bool:
        print(f"Before insertion {self.values=}")
        if not val in self.values:
            self.arr.append(val)
            self.values[val] = len(self.arr) -1
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.values:
            print(f"Before deletion {self.values=}")
            idx = self.values.pop(val)
            print(f"After deletion {self.values=}")
            if idx == len(self.arr) -1:
                self.arr.pop()
                return True
            last_val = self.arr[-1]
            self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
            self.values[last_val] = idx
            self.arr.pop()

            print(f"After deletion {self.values=}")
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.arr)

# ["RandomizedSet","remove","remove","insert","getRandom","remove","insert"]
# [[],[0],[0],[0],[],[0],[0]]
s = RandomizedSet()
print(s.remove(0))
print(s.remove(0))
print(s.insert(0))
print(s.getRandom())
print("last remove")
print(s.remove(0))

print("vals", s.values)
print(s.insert(0))