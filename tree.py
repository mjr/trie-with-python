import logging

from threading import Thread

from node import TrieNode


class TrieTree():
    def __init__(self):
        self.root = TrieNode()
        self.word_list = []

    def setup(self, keys, name):
        # logging.info("Thread %s: starting", name)
        for key in keys:
            self.insert(key)
        # logging.info("Thread %s: finishing", name)

    def insert(self, key):
        node = self.root

        for character in list(key):
            if not node.children.get(character):
                node.children[character] = TrieNode()

            node = node.children[character]

        node.is_word = True

    def search(self, key):
        node = self.root
        found = True

        for character in list(key):
            if not node.children.get(character):
                found = False
                break

            node = node.children[character]

        return node and node.is_word and found

    def run(self, list_words):
        # format = "%(asctime)s: %(message)s"
        # logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

        threads = list()
        for index, word in enumerate(list_words):
            # logging.info("Main    : create and start thread %d.", index)
            x = Thread(target=self.setup, args=(word, index))
            threads.append(x)
            x.start()

        for index, thread in enumerate(threads):
            # logging.info("Main    : before joining thread %d.", index)
            thread.join()
            # logging.info("Main    : thread %d done", index)

    def suggestions(self, node, word):
        if node.is_word:
            self.word_list.append(word)

        for key, value in node.children.items():
            self.suggestions(value, word + key)

    def print_suggestions(self, key):
        node = self.root
        not_found = False
        temp_word = ''

        for character in list(key):
            if not node.children.get(character):
                not_found = True
                break

            temp_word += character
            node = node.children[character]

        if not_found:
            return 0
        elif node.is_word and not node.children:
            return -1

        self.suggestions(node, temp_word)

        for suggestion in sorted(self.word_list, key=len):
            print(suggestion)

        return 1
