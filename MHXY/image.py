import cv2 as cv


class Image:
    def template_match(self, template_path, src_path):
        img = cv.imread(src_path, 0)
        img2 = img.copy()
        template = cv.imread(template_path, 0)
        w, h = template.shape[::-1]
        methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
                   'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
        shape_dict = {}
        for meth in methods:
            img = img2.copy()
            method = eval(meth)
            # Apply template Matching
            res = cv.matchTemplate(img, template, method)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
            if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            shape = (top_left[0], top_left[1], bottom_right[0], bottom_right[1])
            if shape_dict.get(shape) == None:
                shape_dict[shape] = 1;
            else:
                shape_dict[shape] = shape_dict[shape] + 1
            max_shape = max(shape_dict, key=shape_dict.get)
        return max_shape, shape_dict[max_shape]
