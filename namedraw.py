#!/usr/bin/env python
import sys
import random
from argparse import ArgumentParser

def print_loop(names):
  """Print a loop of name drawings."""
  if len(names) == 0:
    return
  for n1, n2 in zip(names, names[1:]):
    print n1, "-->", n2
  print names[-1], "-->", names[0]

def split_loop(names, min_size):
  """Return a 2-tuple of a list of names split into two loops.

  The second item is None when names is the minimum size or can't be divided in
  such a way that it obeys the minimum size.
  """
  lo = min_size
  hi = len(names) - min_size
  if lo > hi:
    return names, None
  pivot = random.randint(0, len(names))
  if pivot < lo or pivot >= hi:
    return names, None
  return names[:pivot], names[pivot:]

def make_loops(names, min_size):
  loops = []
  l1, l2 = split_loop(names, min_size)
  loops.append(l1)
  while not l2 is None:
    l1, l2 = split_loop(l2, min_size)
    loops.append(l1)
  return loops

def main():
  names = sys.argv[1:]
  if len(names) <= 1:
    print "usage:", sys.argv[0], "name name..."
    sys.exit(1)
  random.shuffle(names)
  loops = make_loops(names, 2)
  for loop in loops:
    print_loop(loop)

if __name__ == "__main__":
  main()
