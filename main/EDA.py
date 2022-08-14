import lib.viz as vz

class eda:
    
    def __init__(self, dataset = vz.viz()):
        dataset = vz.viz(dataset)
        dataset.select_options(dataset)


