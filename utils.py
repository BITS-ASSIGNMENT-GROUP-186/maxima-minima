class Utilities:

    def __init__(self, input_file):
        self.input_file = input_file
        self.minima = None
        self.maxima = None

    def create_list_from_input_data(self):
        """
        Method to hold input data read in data compound list
        :return: None
        """
        input_data_list = []
        for data in self.input_file:
            input_data_list.append([int(val) for val in data.strip('\n').split(" ")])
        return input_data_list

    # Divide & Conquer solution to find minimum and maximum number in data list
    def findMinAndMax(self, data, left, right, minimum, maximum):

        # if list contains only one element
        if left == right:  # common comparison
            if minimum > data[right]:  # comparison 1
                minimum = data[right]
            if maximum < data[left]:  # comparison 2
                maximum = data[left]
            return minimum, maximum

        # if list contains only two elements
        if right - left == 1:  # common comparison
            if data[left] < data[right]:  # comparison 1
                if minimum > data[left]:  # comparison 2
                    minimum = data[left]
                if maximum < data[right]:  # comparison 3
                    maximum = data[right]
            else:
                if minimum > data[right]:  # comparison 2
                    minimum = data[right]
                if maximum < data[left]:  # comparison 3
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
        self.minima, self.maxima = self.findMinAndMax(data=data, left=0, right=len(data) - 1, minimum=float('inf'), maximum=-float('inf'))

        if data[0] < data[1]:
            if data.index(self.maxima) == len(data) - 1:
                return 'increasing'
            else:
                return 'maxima'
        else:
            if data.index(self.minima) == len(data) - 1:
                return 'decreasing'
            else:
                return 'minima'

    def get_maxima_minima(self, distribution_type):
        if distribution_type in ['increasing', 'decreasing', 'minima']:
            return self.minima
        else:
            return self.maxima
