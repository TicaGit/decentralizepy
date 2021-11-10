from decentralizepy import utils

class Dataset:
    """
    This class defines the Dataset API.
    All datasets must follow this API.
    """

    def __init__(self, rank="", n_procs="", train_dir="", test_dir="", sizes=""):
        """
        Constructor which reads the data files, instantiates and partitions the dataset
        Parameters
        ----------
        rank : int, optional
            Rank of the current process (to get the partition). Default value is assigned 0
        n_procs : int, optional
            The number of processes among which to divide the data. Default value is assigned 1
        train_dir : str, optional
            Path to the training data files. Required to instantiate the training set
            The training set is partitioned according to n_procs and sizes
        test_dir : str. optional
            Path to the testing data files Required to instantiate the testing set
        sizes : list(int), optional
            A list of fractions specifying how much data to alot each process. Sum of fractions should be 1.0
            By default, each process gets an equal amount.
        """
        self.rank = utils.conditional_value(rank, "", 0)
        self.n_procs = utils.conditional_value(n_procs, "", 1)
        self.train_dir = utils.conditional_value(train_dir, "", None)
        self.test_dir = utils.conditional_value(test_dir, "", None)
        self.sizes = utils.conditional_value(sizes, "", None)
        if self.sizes:
            if type(self.sizes) == str:
                self.sizes = eval(self.sizes)


        if train_dir:
            self.__training__ = True
        else:
            self.__training__ = False

        if test_dir:
            self.__testing__ = True
        else:
            self.__testing__ = False

    def get_trainset(self):
        """
        Function to get the training set
        Returns
        -------
        Dataset
        Raises
        ------
        RuntimeError
            If the training set was not initialized
        """
        raise NotImplementedError

    def get_testset(self):
        """
        Function to get the test set
        Returns
        -------
        Dataset
        Raises
        ------
        RuntimeError
            If the test set was not initialized
        """
        raise NotImplementedError
