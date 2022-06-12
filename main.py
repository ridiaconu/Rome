from routegen import RouteGenerator
from timeit import timeit
import random

TEST = RouteGenerator()
ROMANIA = RouteGenerator()
LARGE = RouteGenerator()
VERY_LARGE = RouteGenerator()

TEST.load_data("samples.json", "test_graph")  # 12 noduri 12 muchii
ROMANIA.load_data("samples.json", "romania")  # 20 noduri 23 muchii (harta Romaniei)


#TEST.print_optimal_route('A', 'G')

orasetxt=open("orase.txt", "r")
orase_list=orasetxt.read()
orase=orase_list.split("\n")
orasetxt.close()

oras_p1=random.choice(orase)
oras_p2=random.choice(orase)
while oras_p1==oras_p2:
  oras_p2=random.choice(orase)
  
print(oras_p1 + " " + oras_p2)
ROMANIA.print_optimal_route(oras_p1, oras_p2)

print(timeit())