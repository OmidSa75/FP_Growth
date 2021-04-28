import numpy as np
from collections import Counter
from copy import deepcopy
from tqdm import tqdm


class FPGrowth:
    def __init__(self, dataset):
        self.dataset = dataset
        self.raw_dataset = dataset.pp_data
        self.data_counts = self.unique_data_with_counts()
        self.counted_data = self.row_counted_dataset()
        self.sort_items = self.data_counts[:, 0]
        self.tree = {}

    def row_counted_dataset(self):
        counted_data = []
        for row in self.raw_dataset:
            counted_data.append(np.array(list(Counter(row).items())))

        return counted_data

    def fit(self):
        for row in tqdm(self.counted_data, desc='Fitting'):
            tree = deepcopy(self.tree)
            tree = self.append_tree(self.sort_items, tree, row)
            self.tree.update(tree)

    def unique_data_with_counts(self):
        arr = []
        dataset = self.dataset()
        for i in range(len(dataset)):
            arr += dataset[i]

        arr, counts = np.unique(arr, return_counts=True, )
        data_counts = np.c_[arr, counts]
        data_counts = np.array(sorted(data_counts, key=lambda x: x[1], reverse=True))
        data_counts = data_counts[data_counts[:, 0] < 10]
        return data_counts

    def append_tree(self, items: np.ndarray, tree: dict, row: np.ndarray):
        if len(items) > 0:
            if items[0] in row[:, 0]:
                if items[0] in tree.keys():
                    tree[items[0]]['count'] += row[row[:, 0] == items[0]][:, 1]
                    tree[items[0]]['leave'].update(self.append_tree(items[1:], tree[items[0]]['leave'], row))
                else:
                    tree[items[0]] = {'count': row[row[:, 0] == items[0]][:, 1], 'leave': {}}
                    tree[items[0]]['leave'] = self.append_tree(items[1:], tree[items[0]]['leave'], row)

                return tree
            else:
                tree.update(self.append_tree(items[1:], {}, row))
                return tree
        else:
            return {}