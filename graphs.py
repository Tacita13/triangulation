import itertools

# Every possible permutation given the number of vertices
def graphs(vertices):
  antichains(list(itertools.permutations(vertices)))

# It computes the antichains of each permutation
def antichains(permutations):
  antichains = []
  for perm in permutations:
    antichains.append(list(non_consecutive_combinator(perm[:-2], 2)))
  antichains.sort()
  new_antichains = list(antichains for antichains,_ in itertools.groupby(antichains))
  sort(new_antichains)

# It gives a pair of the non-consecutive elements in a list
def non_consecutive_combinator(rnge, r, prev=[]):
    if r == 0:
        yield prev
    else:
        for i, item in enumerate(rnge):
            for next_comb in non_consecutive_combinator(rnge[i+2:], r-1, prev+[item]):
                yield next_comb

# Sort antichain lists and pairs of antichains
def sort(antichains_list):
  for antichains in antichains_list:
    for pair in antichains:
      pair.sort()
    antichains.sort()
  remove_duplicates(antichains_list)

# Remove duplicate list of antichains
def remove_duplicates(antichains_list):
  new_list = list()
  for antichain in antichains_list:
    if antichain not in new_list:
      new_list.append(antichain)
  print(len(new_list))

l=[1,2,3,4,5] #10
l=[1,2,3,4,5,6] #180
l=[1,2,3,4,5,6,7] #1260
l=[1,2,3,4,5,6,7,8] #10080
l=[1,2,3,4,5,6,7,8,9]

graphs(l)
