##cache funcationality implematation


#1.clear function to clear least use cache - Cache eviction
#2.useful for history/static dat kind of things only
#3.Job to clear cache incase of expirationtime is set
#4.check max size of cache

import time
import datetime
import random

class CacheImplementation():
    def __init__(self):
        self.cache_dict={}
        self.max_cache_dict_size=10

    def update_cache(self,key,value,duration_in_mins=None):
        if key not in self.cache_dict and len(self.cache_dict)>=self.max_cache_dict_size:
            self.remove_least_used()

        self.cache_dict[key]= {"value":value, "accessed_time": datetime.datetime.now(), "duration": duration_in_mins}

    def remove_least_used(self):
        a = {}
        for key in self.cache_dict:
            a[key] = self.cache_dict[key]["accessed_time"]
        old_key = (min(a, key=a.get))
        del self.cache_dict[old_key]

    def clear_expired_keys(self):
        #print("here",self.cache_dict)
        keys_for_del =[]
        for key in self.cache_dict:
            if self.cache_dict[key]["duration"] is not None:
                print(key)
                if self.cache_dict[key]["accessed_time"]+datetime.timedelta(minutes = self.cache_dict[key]["duration"])<datetime.datetime.now():
                    keys_for_del.append(key)
        #print("keys_for_del : ",keys_for_del)
        for key in keys_for_del:
            del self.cache_dict[key]

#Testing:
sample = {1: {"value": "a","accessed_time":datetime.datetime.now(),"duration":None},
          2: {"value": "b", "accessed_time": datetime.datetime.now(), "duration": None},
          3: {"value": "c", "accessed_time": datetime.datetime.now(), "duration": 1}}
cache_data = CacheImplementation()
cache_data.cache_dict = sample

def func_1(arg):
    if arg in cache_data.cache_dict:
          #print("Found", arg)
          cache_data.cache_dict[arg]["accessed_time"]=datetime.datetime.now()
          return cache_data.cache_dict[arg]["value"]
    result = random.choice("defghijklmopqrstuvwxyz")
    cache_data.update_cache(arg,result)
    #print("Not found",arg)
    return result


print(func_1(4))
print(func_1(4))
print(func_1(1))
time.sleep(61)
cache_data.clear_expired_keys()

print(cache_data.cache_dict)
print(func_1(3))
print(func_1(1))












