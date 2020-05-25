FACTOR = {
    # factor channel index
    'Input_congestion'        : 0,
    'Input_rainfall'          : 1,
    'Input_accident'          : 2,
    'Input_sns'               : 3,   
    'default'                 : 0
}

MAX_FACTOR = {
    'Input_congestion'        : 2600,
    'Input_rainfall'          : 131,
    'Input_sns'               : 1,
    'Input_accident'          : 1,
    'default'                 : 2600,
}

LINK_FACTOR = {
    'Input_congestion'      : (4,5,6,7),
    'Input_rainfall'        : (2,3,6,7),
    'Input_accident'        : (1,3,5,7)
}

BOUNDARY_AREA = {
    0 : [ 20, 80,   50,  100],
    1 : [ 40, 100,  100, 180],
    2 : [ 20, 80,   180, 250]
}

PADDING = {
    0 : [ 0,  60, 30, 80],
    1 : [ 0,  60,  0, 80],
    2 : [ 0,  60,  0, 70]
}

GLOBAL_SIZE_X = [6, 60, 80, 4]
GLOBAL_SIZE_Y = [6, 60, 80, 1]

MAP = {
    'coordinate': {
        'start' : {
            'lat' : 33.588541666667005,
            'lon' : 134.10781250000002
        },
        'offset' : {
            'lat' : 0.0020833333329974835,
            'lon' : 0.003124999999982947
        }
    },
    'total_map' : {
        'size' : {
          'h' : 2000,
          'w' : 2000   
        }        
    },
    'studied_map' : {
        'start' : {
            'lat' : 1402,
            'lon' : 163
        },
        'size' : {
            'h' : 100,
            'w' : 250
        }
    },
    'center' : [50, 168],
    'boundary' : {
        'zone1' : [ [20, 50],  [20, 100], [80, 100],  [80, 50],   [20, 50]  ],
        'zone2' : [ [40, 100], [40, 180], [100, 180], [100, 100], [40, 100] ],
        'zone3' : [ [20, 180], [20, 250], [80, 250],  [80, 180],  [20, 180] ],
        'total' : [ [18, 74],  [18, 253], [102, 253], [102, 74],  [18, 74]  ]
    }
}

