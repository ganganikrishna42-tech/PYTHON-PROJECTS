import numpy as np


class DataAnalytics:

    def __init__(self, array=None):
        self.array = array

    @classmethod
    def from_input(cls, dimensions, shape, values):
        arr = np.array(values).reshape(shape)
        return cls(arr)

    @staticmethod
    def _validate_same_shape(arr1, arr2):
        if arr1.shape != arr2.shape:
            raise ValueError("Arrays must be the same shape for this operation.")

    def get_element(self, index):
        return self.array[index]

    def get_slice(self, row_range, col_range=None):
        if self.array.ndim == 1:
            start, end = row_range
            return self.array[start:end]
        row_start, row_end = row_range
        if col_range is None:
            return self.array[row_start:row_end]
        col_start, col_end = col_range
        return self.array[row_start:row_end, col_start:col_end]

    def combine(self, other, axis=0):
        if self.array.shape[1:] == other.shape[1:] if self.array.ndim > 1 else True:
            return np.concatenate((self.array, other), axis=axis)
        raise ValueError("Arrays are not compatible for combining.")

    def split(self, sections, axis=0):
        return np.array_split(self.array, sections, axis=axis)

    def add(self, other):
        self._validate_same_shape(self.array, other)
        return self.array + other

    def subtract(self, other):
        self._validate_same_shape(self.array, other)
        return self.array - other

    def multiply(self, other):
        self._validate_same_shape(self.array, other)
        return self.array * other

    def divide(self, other):
        self._validate_same_shape(self.array, other)
        return self.array / other

    def dot_product(self, other):
        return np.dot(self.array, other)

    def matrix_multiply(self, other):
        return np.matmul(self.array, other)

    def search(self, value):
        return np.where(self.array == value)

    def sort(self, ascending=True):
        sorted_arr = np.sort(self.array)
        return sorted_arr if ascending else sorted_arr[..., ::-1]

    def filter(self, condition):
        return self.array[condition(self.array)]

    def sum(self):
        return np.sum(self.array)

    def mean(self):
        return np.mean(self.array)

    def median(self):
        return np.median(self.array)

    def std_dev(self):
        return np.std(self.array)

    def variance(self):
        return np.var(self.array)

    def minimum(self):
        return np.min(self.array)

    def maximum(self):
        return np.max(self.array)

    def percentile(self, q):
        return np.percentile(self.array, q)

    def correlation(self, other):
        return np.corrcoef(self.array.flatten(), other.flatten())[0, 1]

    def __repr__(self):
        return f"DataAnalytics(\n{self.array}\n)"
