from util.frequency import FrequencyVector, create_frequency_map, create_pair_frequency_map

def doc_dist(word_list1, word_list2, limit=None):
  freq_map1 = create_frequency_map(word_list1, limit)
  freq_map2 = create_frequency_map(word_list2, limit)

  freq_vec1 = FrequencyVector(freq_map1)
  freq_vec2 = FrequencyVector(freq_map2)

  return freq_vec1.angle(freq_vec2)

def doc_dist_pairs(word_list1, word_list2):
  freq_map1 = create_pair_frequency_map(word_list1)
  freq_map2 = create_pair_frequency_map(word_list2)

  freq_vec1 = FrequencyVector(freq_map1)
  freq_vec2 = FrequencyVector(freq_map2)

  return freq_vec1.angle(freq_vec2)
