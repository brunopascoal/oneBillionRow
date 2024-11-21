from csv import reader
from collections import defaultdict
import time

from pathlib import Path
def process_tempeature(path_txt: Path):
  print("Start...")

  start_time = time.time()

  tempeature_per_station = defaultdict(list)

  with open(path_txt, 'r', encoding="UTF-8") as file:
    _reader = reader(file, delimiter=";")
    for row in _reader:
      name_station, tempeature = str(row[0]), float(row[1])
      tempeature_per_station[name_station].append(tempeature)
  print("Processing finished")

  results = {}

  for station, tempeatures in tempeature_per_station.items():
    min_temp = min(tempeatures)
    mean_temp = sum(tempeatures) / len(tempeatures)
    max_temp = max(tempeatures)
    results[station] = (min_temp, mean_temp, max_temp)

  sorted_results = dict(sorted(results.items()))

  end_time = time.time()
  print(f"Finished in {end_time - start_time}")

  return sorted_results

if __name__ == "__main__":
  path_txt = 'data/measurements.txt'
  results = process_tempeature(path_txt)

