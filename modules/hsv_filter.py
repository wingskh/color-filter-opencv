import cv2
import numpy as np
from constants.window import HEIGHT, WIDTH
from helpers.log_helper import clear_console
from enums.filter_param import FilterParam


class HSVFilter:
    def __init__(self, img):
        self.img = cv2.resize(img, (WIDTH, HEIGHT))
        self.hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(self.hsv)
        self.filter_map = {
            FilterParam.MIN_H: np.min(h),
            FilterParam.MAX_H: np.max(h),
            FilterParam.MIN_S: np.min(s),
            FilterParam.MAX_S: np.max(s),
            FilterParam.MIN_V: np.min(v),
            FilterParam.MAX_V: np.max(v),
        }
        self.filtered_hsv = self.hsv

    def update_filter(self, filter_param, value):
        self.filter_map[filter_param] = value
        print("Filter Param:", filter_param, "Value:", self.filter_map[filter_param])

    def get_filter_param(self, filter_param):
        return self.filter_map[filter_param]

    def update_image(self):
        lower = np.array(
            [
                self.get_filter_param(FilterParam.MIN_H),
                self.get_filter_param(FilterParam.MIN_S),
                self.get_filter_param(FilterParam.MIN_V),
            ],
            dtype=np.uint8,
        )
        upper = np.array(
            [
                self.get_filter_param(FilterParam.MAX_H),
                self.get_filter_param(FilterParam.MAX_S),
                self.get_filter_param(FilterParam.MAX_V),
            ],
            dtype=np.uint8,
        )
        # clear_console()
        # print("Filter Lower:", lower)
        # print("Filter Upper:", upper)
        mask = cv2.inRange(self.hsv, lower, upper)
        self.filtered_hsv = cv2.bitwise_and(self.img, self.img, mask=mask)
