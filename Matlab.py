import numpy as np
import matlab.engine


def error(x,y,z):

    eng = matlab.engine.start_matlab()
    eng.error_volume_main(x,y,z)
    
    """
    return {
            "error": 0.05,
            "volume": 500,
            "data": np.array([[2, 3, 2],
                              [2, 3, 4],
                              [2, 1, 2]]),
            "map" : np.array([[0, 1, 0],
                              [1, 0, 1],
                              [0, 1, 0]]),
            "error_list": np.array([1,2,3,4,5]),
            "start_count": 1
            }
    """

def pile(fill_pts, draw_pts, size, repose):

    eng = matlab.engine.start_matlab()
    return eng.abelian_pile(fill_pts, draw_pts, size, repose)
    """
    return {"x": np.array([[1, 2, 3],
                           [1, 2, 3],
                           [1, 2, 3]]),
            "y": np.array([[1, 1, 1],
                           [2, 2, 2],
                           [3, 3, 3]]),
            "z": np.array([[2, 3, 2],
                           [2, 3, 4],
                           [2, 1, 2]])} # z locales
    """

def pile2(fill_pts, draw_pts, size, repose):

    return {"x": np.array([]),
            "y": np.array([]),
            "z": np.array([])} # z locales


