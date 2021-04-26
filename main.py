from dataset import Dataset
from fp_growth import FPGrowth


if __name__ == '__main__':
    dataset = Dataset('Dataset.txt')
    print(dataset())
