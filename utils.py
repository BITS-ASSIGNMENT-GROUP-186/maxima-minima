class Utilities:

    def __init__(self, input_file):
        self.input_file = input_file
        self.minima = None
        self.maxima = None

    def create_list_from_input_data(self):
        """
        Method to hold input data read in data compound list
        :return: compound list which holds the list of integers
        """
        input_data_list = []
        for data in self.input_file:
            if data != "\n":
                row = []
                for val in data.strip('\n').split(" "):
                    if not val.isnumeric():
                        row = []
                        break
                    row.append(int(val))
                input_data_list.append(row)
            else:
                input_data_list.append("")
        return input_data_list

    # Divide & Conquer solution to find minimum and maximum number in data list
    def findMinAndMax(self, data, left, right, minimum, maximum):
        """
        Method to find maxima and minima from the given list of integers using divide and conquer strategy
        :param data: input list
        :param left: leftmost element of the list
        :param right: rightmost element of the list
        :param minimum: minimum elem of the list
        :param maximum: maximum elem of the list
        :return: minimum and maxima from the given list
        """
        # if list contains only one element
        if left == right:  # common comparison
            if minimum > data[right]:  # comparison 1
                minimum = data[right]
            if maximum < data[left]:  # comparison 2
                maximum = data[left]
            return minimum, maximum

        # find mid element
        mid = (left + right) // 2

        # recur for left sublist
        minimum, maximum = self.findMinAndMax(data, left, mid, minimum, maximum)

        # recur for right sublist
        minimum, maximum = self.findMinAndMax(data, mid + 1, right, minimum, maximum)

        return minimum, maximum
        
    def get_distribution_type(self, data):
        """
        Method to get the distribution type based on the list of integers indicating plot points
        :param data: list of integers
        :return: distribution type
        """
        self.minima, self.maxima = self.findMinAndMax(data=data,
                                                      left=0,
                                                      right=len(data) - 1,
                                                      minimum=float('inf'),
                                                      maximum=-float('inf'))

        if data[0] < data[1]:
            return 'increasing' if data.index(self.maxima) == len(data) - 1 else 'maxima'
        else:
            return 'decreasing' if data.index(self.minima) == len(data) - 1 else 'minima'

    def get_maxima_minima(self, distribution_type):
        """
        Method to return the minima or maxima based on given distribution type
        :param distribution_type: distribution type
        :return: Maxima or minima value in integer
        """
        return self.minima if distribution_type in ['increasing', 'decreasing', 'minima'] else self.maxima
