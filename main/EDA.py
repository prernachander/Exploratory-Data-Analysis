import lib.viz as vz
default = 'data/iris.csv'
class eda:
    
    def __init__(self, dataset=default):
        dataset = vz.viz(dataset)
        dataset.select_options(dataset)


