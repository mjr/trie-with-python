from itertools import chain
from time import time
from tree import TrieTree


PATHNAME = 'dictionary.txt'

def get_list_dictionary():
    list_dictionary = {}

    with open(PATHNAME) as fp:
        line = fp.readline()
        while line:
            word = line.strip().lower()
            if not list_dictionary.get(word[0]):
                list_dictionary[word[0]] = [word]
            else:
                list_dictionary[word[0]].append(word)
            line = fp.readline()

    return list_dictionary


def main_sequential(trie_tree):
    list_dictionary = get_list_dictionary()

    list_of_lists = list(list_dictionary.values())
    flattened_list = list(chain(*list_of_lists))
    trie_tree.setup(flattened_list, 1)


def main_thread(trie_tree):
    list_dictionary = get_list_dictionary()

    list_of_lists = list(list_dictionary.values())
    trie_tree.run(list_of_lists)


if __name__ == '__main__':
    trie_tree = TrieTree()
    start_time = time()
    main_sequential(trie_tree)
    # main_thread(trie_tree)
    end_time = time()
    print(f"--- {(end_time - start_time)} seconds ---")

    result = trie_tree.search("lovee")
    if result:
        print('find.')
    else:
        print('not found.')

    # result = trie_tree.print_suggestions("love")
    # if result == -1:
    #     print("No other strings found with this prefix\n")
    # elif result == 0:
    #     print("No string found with this prefix\n")
