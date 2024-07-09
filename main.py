import cv2
import numpy as np
from constants.window import HEIGHT, TOOLBAR_HEIGHT, WIDTH, INPUT_IMAGE_PATH
from enums.filter_param import FilterParam
from modules.hsv_filter import HSVFilter
import copy

filter_max_value_map = {
    FilterParam.MIN_H: 179,
    FilterParam.MAX_H: 179,
    FilterParam.MIN_S: 255,
    FilterParam.MAX_S: 255,
    FilterParam.MIN_V: 255,
    FilterParam.MAX_V: 255,
}

img = cv2.imread(INPUT_IMAGE_PATH)
hsv_filter = HSVFilter(img)
cv2.namedWindow("Color Filter", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Color Filter", WIDTH, HEIGHT + TOOLBAR_HEIGHT)

for filter_param in FilterParam:
    cv2.createTrackbar(
        filter_param.value,
        "Color Filter",
        hsv_filter.get_filter_param(filter_param),
        filter_max_value_map[filter_param],
        lambda x, fp=filter_param: hsv_filter.update_filter(fp, x),
    )

while True:
    hsv_filter.update_image()
    cv2.imshow("Color Filter", hsv_filter.filtered_hsv)

    if (
        cv2.waitKey(1) & 0xFF == 27
        or cv2.getWindowProperty("Color Filter", cv2.WND_PROP_VISIBLE) < 1
    ):
        break
