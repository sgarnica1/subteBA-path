VELOCITY = 400  # la velocidad media pasó de 24 km/hora a metros/minutos

STATIONS = {
    "ALBERTI": "ALBERTI",
    "PASCO": "PASCO",
    "CONGRESO": "CONGRESO",
    "SAENZ_PENA": "SAENZ_PENA",
    "LIMA": "LIMA",
    "PIEDRAS": "PIEDRAS",
    "PERU": "PERU",
    "PLAZA_DE_MAYO": "PLAZA_DE_MAYO",
    "PASTEUR": "PASTEUR",
    "CALLAO_B": "CALLAO_B",
    "URUGUAY": "URUGUAY",
    "CARLOS_PELLEGRINI": "CARLOS_PELLEGRINI",
    "FLORIDA": "FLORIDA",
    "LEANDRO_N_ALEM": "LEANDRO_N_ALEM",
    "RETIRO": "RETIRO",
    "GENERAL_SAN_MARTIN": "GENERAL_SAN_MARTIN",
    "LAVALLE": "LAVALLE",
    "DIAGONAL_NORTE": "DIAGONAL_NORTE",
    "AVENIDA_DE_MAYO": "AVENIDA_DE_MAYO",
    "MORENO": "MORENO",
    "INDEPENDENCIA_C": "INDEPENDENCIA_C",
    "SAN_JUAN": "SAN_JUAN",
    "CONSTITUCION": "CONSTITUCION",
    "FACULTAD_DE_MEDICINA": "FACULTAD_DE_MEDICINA",
    "CALLAO_D": "CALLAO_D",
    "TRIBUNALES": "TRIBUNALES",
    "9_DE_JULIO": "9_DE_JULIO",
    "CATEDRAL": "CATEDRAL",
    "PICHINCHA": "PICHINCHA",
    "ENTRE_RIOS": "ENTRE_RIOS",
    "SAN_JOSE": "SAN_JOSE",
    "INDEPENDENCIA_E": "INDEPENDENCIA_E",
    "BELGRANO": "BELGRANO",
    "BOLIVAR": "BOLIVAR",
}

LINE_NAMES = {
    "LINEA_A": "Línea A",
    "LINEA_B": "Línea B",
    "LINEA_C": "Línea C",
    "LINEA_D": "Línea D",
    "LINEA_E": "Línea E",
}

STATIONS_POSITION = {
    # LÍNEA A
    STATIONS["ALBERTI"]: {
        "name": STATIONS["ALBERTI"],
        "position": (0, 9),
        "line": LINE_NAMES["LINEA_A"],
    },
    STATIONS["PASCO"]: {
        "name": STATIONS["PASCO"],
        "position": (1, 9),
        "line": LINE_NAMES["LINEA_A"],
    },
    STATIONS["CONGRESO"]: {
        "name": STATIONS["CONGRESO"],
        "position": (2, 9),
        "line": LINE_NAMES["LINEA_A"],
    },
    STATIONS["SAENZ_PENA"]: {
        "name": STATIONS["SAENZ_PENA"],
        "position": (3, 9),
        "line": LINE_NAMES["LINEA_A"],
    },
    STATIONS["LIMA"]: {
        "name": STATIONS["LIMA"],
        "position": (4, 9),
        "line": LINE_NAMES["LINEA_A"],
    },
    STATIONS["PIEDRAS"]: {
        "name": STATIONS["PIEDRAS"],
        "position": (5, 9),
        "line": LINE_NAMES["LINEA_A"],
    },
    STATIONS["PERU"]: {
        "name": STATIONS["PERU"],
        "position": (6, 9),
        "line": LINE_NAMES["LINEA_A"],
    },
    STATIONS["PLAZA_DE_MAYO"]: {
        "name": STATIONS["PLAZA_DE_MAYO"],
        "position": (7, 9),
        "line": LINE_NAMES["LINEA_A"],
    },
    # LÍNEA B
    STATIONS["PASTEUR"]: {
        "name": STATIONS["PASTEUR"],
        "position": (0.5, 11.5),
        "line": LINE_NAMES["LINEA_B"],
    },
    STATIONS["CALLAO_B"]: {
        "name": STATIONS["CALLAO_B"],
        "position": (2, 11.5),
        "line": LINE_NAMES["LINEA_B"],
    },
    STATIONS["URUGUAY"]: {
        "name": STATIONS["URUGUAY"],
        "position": (3, 11.5),
        "line": LINE_NAMES["LINEA_B"],
    },
    STATIONS["CARLOS_PELLEGRINI"]: {
        "name": STATIONS["CARLOS_PELLEGRINI"],
        "position": (5, 11.5),
        "line": LINE_NAMES["LINEA_B"],
    },
    STATIONS["FLORIDA"]: {
        "name": STATIONS["FLORIDA"],
        "position": (6, 11.5),
        "line": LINE_NAMES["LINEA_B"],
    },
    STATIONS["LEANDRO_N_ALEM"]: {
        "name": STATIONS["LEANDRO_N_ALEM"],
        "position": (7, 11.5),
        "line": LINE_NAMES["LINEA_B"],
    },
    # LÍNEA C
    STATIONS["RETIRO"]: {
        "name": STATIONS["RETIRO"],
        "position": (7, 15),
        "line": LINE_NAMES["LINEA_C"],
    },
    STATIONS["GENERAL_SAN_MARTIN"]: {
        "name": STATIONS["GENERAL_SAN_MARTIN"],
        "position": (6.5, 14),
        "line": LINE_NAMES["LINEA_C"],
    },
    STATIONS["LAVALLE"]: {
        "name": STATIONS["LAVALLE"],
        "position": (5.5, 12),
        "line": LINE_NAMES["LINEA_C"],
    },
    STATIONS["DIAGONAL_NORTE"]: {
        "name": STATIONS["DIAGONAL_NORTE"],
        "position": (5, 10.5),
        "line": LINE_NAMES["LINEA_C"],
    },
    STATIONS["AVENIDA_DE_MAYO"]: {
        "name": STATIONS["AVENIDA_DE_MAYO"],
        "position": (4.5, 9),
        "line": LINE_NAMES["LINEA_C"],
    },
    STATIONS["MORENO"]: {
        "name": STATIONS["MORENO"],
        "position": (4.5, 7.5),
        "line": LINE_NAMES["LINEA_C"],
    },
    STATIONS["INDEPENDENCIA_C"]: {
        "name": STATIONS["INDEPENDENCIA_C"],
        "position": (4.5, 5),
        "line": LINE_NAMES["LINEA_C"],
    },
    STATIONS["SAN_JUAN"]: {
        "name": STATIONS["SAN_JUAN"],
        "position": (4.5, 3),
        "line": LINE_NAMES["LINEA_C"],
    },
    STATIONS["CONSTITUCION"]: {
        "name": STATIONS["CONSTITUCION"],
        "position": (4.5, 0),
        "line": LINE_NAMES["LINEA_C"],
    },
    # LÍNEA D
    STATIONS["FACULTAD_DE_MEDICINA"]: {
        "name": STATIONS["FACULTAD_DE_MEDICINA"],
        "position": (0, 13),
        "line": LINE_NAMES["LINEA_D"],
    },
    STATIONS["CALLAO_D"]: {
        "name": STATIONS["CALLAO_D"],
        "position": (2, 13),
        "line": LINE_NAMES["LINEA_D"],
    },
    STATIONS["TRIBUNALES"]: {
        "name": STATIONS["TRIBUNALES"],
        "position": (3, 12),
        "line": LINE_NAMES["LINEA_D"],
    },
    STATIONS["9_DE_JULIO"]: {
        "name": STATIONS["9_DE_JULIO"],
        "position": (5, 11),
        "line": LINE_NAMES["LINEA_D"],
    },
    STATIONS["CATEDRAL"]: {
        "name": STATIONS["CATEDRAL"],
        "position": (6, 10),
        "line": LINE_NAMES["LINEA_D"],
    },
    # LÍNEA E
    STATIONS["PICHINCHA"]: {
        "name": STATIONS["PICHINCHA"],
        "position": (0.5, 3),
        "line": LINE_NAMES["LINEA_E"],
    },
    STATIONS["ENTRE_RIOS"]: {
        "name": STATIONS["ENTRE_RIOS"],
        "position": (2, 3),
        "line": LINE_NAMES["LINEA_E"],
    },
    STATIONS["SAN_JOSE"]: {
        "name": STATIONS["SAN_JOSE"],
        "position": (3, 3),
        "line": LINE_NAMES["LINEA_E"],
    },
    STATIONS["INDEPENDENCIA_E"]: {
        "name": STATIONS["INDEPENDENCIA_E"],
        "position": (3.5, 5),
        "line": LINE_NAMES["LINEA_E"],
    },
    STATIONS["BELGRANO"]: {
        "name": STATIONS["BELGRANO"],
        "position": (5, 7),
        "line": LINE_NAMES["LINEA_E"],
    },
    STATIONS["BOLIVAR"]: {
        "name": STATIONS["BOLIVAR"],
        "position": (6, 8),
        "line": LINE_NAMES["LINEA_E"],
    },
}

CONNECTIONS = [
    # Línea A
    (STATIONS["ALBERTI"], STATIONS["PASCO"]),
    (STATIONS["PASCO"], STATIONS["CONGRESO"]),
    (STATIONS["CONGRESO"], STATIONS["SAENZ_PENA"]),
    (STATIONS["SAENZ_PENA"], STATIONS["LIMA"]),
    (STATIONS["LIMA"], STATIONS["PIEDRAS"]),
    (STATIONS["PIEDRAS"], STATIONS["PERU"]),
    (STATIONS["PERU"], STATIONS["PLAZA_DE_MAYO"]),
    # Línea B
    (STATIONS["PASTEUR"], STATIONS["CALLAO_B"]),
    (STATIONS["CALLAO_B"], STATIONS["URUGUAY"]),
    (STATIONS["URUGUAY"], STATIONS["CARLOS_PELLEGRINI"]),
    (STATIONS["CARLOS_PELLEGRINI"], STATIONS["FLORIDA"]),
    (STATIONS["FLORIDA"], STATIONS["LEANDRO_N_ALEM"]),
    # Línea C
    (STATIONS["RETIRO"], STATIONS["GENERAL_SAN_MARTIN"]),
    (STATIONS["GENERAL_SAN_MARTIN"], STATIONS["LAVALLE"]),
    (STATIONS["LAVALLE"], STATIONS["DIAGONAL_NORTE"]),
    (STATIONS["DIAGONAL_NORTE"], STATIONS["AVENIDA_DE_MAYO"]),
    (STATIONS["AVENIDA_DE_MAYO"], STATIONS["MORENO"]),
    (STATIONS["MORENO"], STATIONS["INDEPENDENCIA_C"]),
    (STATIONS["INDEPENDENCIA_C"], STATIONS["SAN_JUAN"]),
    (STATIONS["SAN_JUAN"], STATIONS["CONSTITUCION"]),
    # Línea D
    (STATIONS["FACULTAD_DE_MEDICINA"], STATIONS["CALLAO_D"]),
    (STATIONS["CALLAO_D"], STATIONS["TRIBUNALES"]),
    (STATIONS["TRIBUNALES"], STATIONS["9_DE_JULIO"]),
    (STATIONS["9_DE_JULIO"], STATIONS["CATEDRAL"]),
    # Línea E
    (STATIONS["PICHINCHA"], STATIONS["ENTRE_RIOS"]),
    (STATIONS["ENTRE_RIOS"], STATIONS["SAN_JOSE"]),
    (STATIONS["SAN_JOSE"], STATIONS["INDEPENDENCIA_E"]),
    (STATIONS["INDEPENDENCIA_E"], STATIONS["BELGRANO"]),
    (STATIONS["BELGRANO"], STATIONS["BOLIVAR"]),
    # Transbordos
    (STATIONS["BOLIVAR"], STATIONS["PERU"]),
    (STATIONS["BOLIVAR"], STATIONS["CATEDRAL"]),
    (STATIONS["CATEDRAL"], STATIONS["PERU"]),
    (STATIONS["INDEPENDENCIA_C"], STATIONS["INDEPENDENCIA_E"]),
    (STATIONS["LIMA"], STATIONS["AVENIDA_DE_MAYO"]),
    (STATIONS["DIAGONAL_NORTE"], STATIONS["9_DE_JULIO"]),
    (STATIONS["DIAGONAL_NORTE"], STATIONS["CARLOS_PELLEGRINI"]),
    (STATIONS["9_DE_JULIO"], STATIONS["CARLOS_PELLEGRINI"]),
]

LINE_STATIONS = {
    "LINEA_A": [
        STATIONS["ALBERTI"],
        STATIONS["PASCO"],
        STATIONS["CONGRESO"],
        STATIONS["SAENZ_PENA"],
        STATIONS["LIMA"],
        STATIONS["PIEDRAS"],
        STATIONS["PERU"],
        STATIONS["PLAZA_DE_MAYO"],
    ],
    "LINEA_B": [
        STATIONS["PASTEUR"],
        STATIONS["CALLAO_B"],
        STATIONS["URUGUAY"],
        STATIONS["CARLOS_PELLEGRINI"],
        STATIONS["FLORIDA"],
        STATIONS["LEANDRO_N_ALEM"],
    ],
    "LINEA_C": [
        STATIONS["RETIRO"],
        STATIONS["GENERAL_SAN_MARTIN"],
        STATIONS["LAVALLE"],
        STATIONS["DIAGONAL_NORTE"],
        STATIONS["AVENIDA_DE_MAYO"],
        STATIONS["MORENO"],
        STATIONS["INDEPENDENCIA_C"],
        STATIONS["SAN_JUAN"],
        STATIONS["CONSTITUCION"],
    ],
    "LINEA_D": [
        STATIONS["FACULTAD_DE_MEDICINA"],
        STATIONS["CALLAO_D"],
        STATIONS["TRIBUNALES"],
        STATIONS["9_DE_JULIO"],
        STATIONS["CATEDRAL"],
    ],
    "LINEA_E": [
        STATIONS["PICHINCHA"],
        STATIONS["ENTRE_RIOS"],
        STATIONS["SAN_JOSE"],
        STATIONS["INDEPENDENCIA_E"],
        STATIONS["BELGRANO"],
        STATIONS["BOLIVAR"],
    ],
}
