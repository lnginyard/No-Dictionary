#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Lorenzo Ginyard, resources(Jason Hoyt, Geeks4geeks, w3schools)'


class Node:
    def __init__(self, key, value=None):
        """Node identified with key and value"""
        self.hash = hash(key)
        self.key = key
        self.value = value

    def __repr__(self):
        """prints a human-readable representation of its key/value"""
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        '''
        Compare Node class to other objects using the `==` operator.
        '''
        #
        return self.key == other.key


class NoDict:
    def __init__(self, num_buckets=10):
        """ implements the key features of a dictionary."""
        self.size = num_buckets
        self.buckets = [[] for _ in range(num_buckets)]

    def __repr__(self):
        """
        Return a string representing the NoDict contents.
        """
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i,
                          bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """Creates new key/value"""
        new_node = Node(key, value)
        bucket = self.buckets[new_node.hash % self.size]
        for key_value in bucket:
            if key_value == new_node:
                bucket.remove(key_value)
                break
        bucket.append(new_node)
        return

    def get(self, key):
        """Gets key /value"""
        node_to_find = Node(key)
        current_bucket = self.buckets[node_to_find.hash % self.size]
        for node in current_bucket:
            if node == node_to_find:
                return node.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        """getting key item"""
        return self.get(key)

    def __setitem__(self, key, value):
        """setting key item"""
        return self.add(key, value)
