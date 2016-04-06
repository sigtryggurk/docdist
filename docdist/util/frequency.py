import math

class FrequencyVector:
  def __init__(self, freq_map):
    self.freq_map = freq_map
    self.values = set(freq_map.keys())
    self.length = self.length()

  def dot(self, other):
    dotproduct = 0
    for item in self.values.intersection(other.values):
      dotproduct += self.freq_map[item] * other.freq_map[item]
    return dotproduct

  def __mul__(self, other):
    return self.dot(other)

  def length(self):
    return math.sqrt(self * self)

  def angle(self, other):
    return math.acos((self * other)/(self.length * other.length))

def create_frequency_map(items, limit=None):
  freq_map = {}
  for item in items:
    freq_map[item] = freq_map.get(item, 0) + 1
  if limit:
    freq_map = nlargest(freq_map, limit)
  return freq_map

def create_pair_frequency_map(items):
  freq_map = {}
  prev = items[0]
  for index, cur in enumerate(items[1:]):
    pair = (prev, cur)
    freq_map[pair] = freq_map.get(pair, 0) + 1
    prev = cur
  return freq_map

def nlargest(freq_map, n):
  freq_map_list = freq_map.items()
  freq_map_list.sort(key = lambda k: (-k[1], k[0]))
  nlargest = dict(freq_map_list[:n])
  return nlargest
