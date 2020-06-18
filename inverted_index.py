"""
Copyright 2020, Dave Huh
smheo2@illinois.edu
"""


import sys
import re

class InvertedIndex:
    """
    A simple inverted index with inverted lists as explained in Lecture 1.
    """

    def __init__(self):
        """
        Construct an empty inverted index.
        """

        self.inverted_lists = {}

    def build_from_file(self, file_name):
        """
        Build inverted index from given file, with one text record per line.
        """

        with open(file_name) as file:
            record_id = 0
            for line in file:
                record_id += 1
                words = re.split("[^a-zA-Z]+", line)
                for word in words:
                    word = word.lower()
                    if len(word) > 0:
                        if word not in self.inverted_lists:
                            self.inverted_lists[word] = []
                        if record_id not in self.inverted_lists[word]:
                            self.inverted_lists[word].append([record_id, 1])
                        else:
                            tmp = self.inverted_lists[word]
                            idx = tmp.index(record_id)
                            tmp[idx, 2] += 1
                            self.inverted_lists[word] = tmp
            print(sorted(self.inverted_lists.items()))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 inverted_index.py <file>")
        sys.exit(1)
    file_name = sys.argv[1]
    ii = InvertedIndex()
    ii.build_from_file(file_name)
