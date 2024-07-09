from enum import Enum


class FilterParam(Enum):
    MIN_H = "Min Hue"
    MIN_S = "Min Sat"
    MIN_V = "Min Val"
    MAX_H = "Max Hue"
    MAX_S = "Max Sat"
    MAX_V = "Max Val"