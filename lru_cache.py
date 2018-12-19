
from datetime import datetime
from collections import OrderedDict  # Do I really need this ?


class LRUCacher(object):

    def __init__(self, max_size=5):
        self.max_size = max_size
        self.max_life_seconds = 200
        self.entries = OrderedDict()
        self.accesses = OrderedDict()

    def __setitem__(self, key, value):
        self.entries[key] = {"value": value, "last_used": datetime.now()}
        if key not in self.accesses:
            self.accesses[key] = 0
        self.accesses[key] += 1
        self.check_if_max()

    def __getitem__(self, key):
        if key in self.entries:
            self.entries[key]["last_used"] = datetime.now()
            self.accesses[key] += 1
        raise KeyError

    def __delete__(self, key):
        if key in self.entries:
            del self.entries[key]
            del self.accesses[key]

    def clean(self, keys):
        sorted_accesses = sorted(self.accesses.items(), key=lambda x: x[1])
        self.__delete__(sorted_accesses[0][0])

    def size(self):
        return len(self.entries)

    def clear(self):
        self.entries = OrderedDict()

    def check_items_expirations(self):
        current_time = datetime.now()
        for key, entry in self.entries:
            entry_time = entry["last_used"]
            total_entry_life_delta = (entry_time - current_time).total_seconds()
            if total_entry_life_delta > self.max_life_seconds:
                del self.entries[key]

    def check_if_max(self):
        if len(self.entries) > self.max_size:
            self.check_items_expirations()

        while len(self.entries) < self.max_size:
            self.clean()
