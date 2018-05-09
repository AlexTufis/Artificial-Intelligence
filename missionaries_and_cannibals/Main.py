from missionaries_and_cannibals import *
from search import *


def main():
    problem = VCL((3,3,'S',0,0),(0,0,'D',3,3))

    path = breadth_first_tree_search(problem).solution()
    print(path, '\n')

if __name__ == "__main__":
    main()
