from dataset import Dataset
from fp_growth import FPGrowth
from pprint import pprint


if __name__ == '__main__':
    dataset = Dataset('Dataset.txt')
    fp_growth = FPGrowth(dataset)

    fp_growth.fit()
    pprint(fp_growth.tree)
