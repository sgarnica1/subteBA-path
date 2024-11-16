# config.py

VELOCIDAD = 400  # la velocidad media pasó de 24 km/hora a metros/minutos

ESTACIONES = {
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

LINEAS = {
    "LINEA_A": "Línea A",
    "LINEA_B": "Línea B",
    "LINEA_C": "Línea C",
    "LINEA_D": "Línea D",
    "LINEA_E": "Línea E",
}

ESTACIONES_POSICIONES = {
    # LÍNEA A
    ESTACIONES["ALBERTI"]: {
        "name": ESTACIONES["ALBERTI"],
        "position": (0, 9),
        "line": LINEAS["LINEA_A"],
    },
    ESTACIONES["PASCO"]: {
        "name": ESTACIONES["PASCO"],
        "position": (1, 9),
        "line": LINEAS["LINEA_A"],
    },
    ESTACIONES["CONGRESO"]: {
        "name": ESTACIONES["CONGRESO"],
        "position": (2, 9),
        "line": LINEAS["LINEA_A"],
    },
    ESTACIONES["SAENZ_PENA"]: {
        "name": ESTACIONES["SAENZ_PENA"],
        "position": (3, 9),
        "line": LINEAS["LINEA_A"],
    },
    ESTACIONES["LIMA"]: {
        "name": ESTACIONES["LIMA"],
        "position": (4, 9),
        "line": LINEAS["LINEA_A"],
    },
    ESTACIONES["PIEDRAS"]: {
        "name": ESTACIONES["PIEDRAS"],
        "position": (5, 9),
        "line": LINEAS["LINEA_A"],
    },
    ESTACIONES["PERU"]: {
        "name": ESTACIONES["PERU"],
        "position": (6, 9),
        "line": LINEAS["LINEA_A"],
    },
    ESTACIONES["PLAZA_DE_MAYO"]: {
        "name": ESTACIONES["PLAZA_DE_MAYO"],
        "position": (7, 9),
        "line": LINEAS["LINEA_A"],
    },
    # LÍNEA B
    ESTACIONES["PASTEUR"]: {
        "name": ESTACIONES["PASTEUR"],
        "position": (0.5, 11.5),
        "line": LINEAS["LINEA_B"],
    },
    ESTACIONES["CALLAO_B"]: {
        "name": ESTACIONES["CALLAO_B"],
        "position": (2, 11.5),
        "line": LINEAS["LINEA_B"],
    },
    ESTACIONES["URUGUAY"]: {
        "name": ESTACIONES["URUGUAY"],
        "position": (3, 11.5),
        "line": LINEAS["LINEA_B"],
    },
    ESTACIONES["CARLOS_PELLEGRINI"]: {
        "name": ESTACIONES["CARLOS_PELLEGRINI"],
        "position": (5, 11.5),
        "line": LINEAS["LINEA_B"],
    },
    ESTACIONES["FLORIDA"]: {
        "name": ESTACIONES["FLORIDA"],
        "position": (6, 11.5),
        "line": LINEAS["LINEA_B"],
    },
    ESTACIONES["LEANDRO_N_ALEM"]: {
        "name": ESTACIONES["LEANDRO_N_ALEM"],
        "position": (7, 11.5),
        "line": LINEAS["LINEA_B"],
    },
    # LÍNEA C
    ESTACIONES["RETIRO"]: {
        "name": ESTACIONES["RETIRO"],
        "position": (7, 15),
        "line": LINEAS["LINEA_C"],
    },
    ESTACIONES["GENERAL_SAN_MARTIN"]: {
        "name": ESTACIONES["GENERAL_SAN_MARTIN"],
        "position": (6.5, 14),
        "line": LINEAS["LINEA_C"],
    },
    ESTACIONES["LAVALLE"]: {
        "name": ESTACIONES["LAVALLE"],
        "position": (5.5, 12),
        "line": LINEAS["LINEA_C"],
    },
    ESTACIONES["DIAGONAL_NORTE"]: {
        "name": ESTACIONES["DIAGONAL_NORTE"],
        "position": (5, 10.5),
        "line": LINEAS["LINEA_C"],
    },
    ESTACIONES["AVENIDA_DE_MAYO"]: {
        "name": ESTACIONES["AVENIDA_DE_MAYO"],
        "position": (4.5, 9),
        "line": LINEAS["LINEA_C"],
    },
    ESTACIONES["MORENO"]: {
        "name": ESTACIONES["MORENO"],
        "position": (4.5, 7.5),
        "line": LINEAS["LINEA_C"],
    },
    ESTACIONES["INDEPENDENCIA_C"]: {
        "name": ESTACIONES["INDEPENDENCIA_C"],
        "position": (4.5, 5),
        "line": LINEAS["LINEA_C"],
    },
    ESTACIONES["SAN_JUAN"]: {
        "name": ESTACIONES["SAN_JUAN"],
        "position": (4.5, 3),
        "line": LINEAS["LINEA_C"],
    },
    ESTACIONES["CONSTITUCION"]: {
        "name": ESTACIONES["CONSTITUCION"],
        "position": (4.5, 0),
        "line": LINEAS["LINEA_C"],
    },
    # LÍNEA D
    ESTACIONES["FACULTAD_DE_MEDICINA"]: {
        "name": ESTACIONES["FACULTAD_DE_MEDICINA"],
        "position": (0, 13),
        "line": LINEAS["LINEA_D"],
    },
    ESTACIONES["CALLAO_D"]: {
        "name": ESTACIONES["CALLAO_D"],
        "position": (2, 13),
        "line": LINEAS["LINEA_D"],
    },
    ESTACIONES["TRIBUNALES"]: {
        "name": ESTACIONES["TRIBUNALES"],
        "position": (3, 12),
        "line": LINEAS["LINEA_D"],
    },
    ESTACIONES["9_DE_JULIO"]: {
        "name": ESTACIONES["9_DE_JULIO"],
        "position": (5, 11),
        "line": LINEAS["LINEA_D"],
    },
    ESTACIONES["CATEDRAL"]: {
        "name": ESTACIONES["CATEDRAL"],
        "position": (6, 10),
        "line": LINEAS["LINEA_D"],
    },
    # LÍNEA E
    ESTACIONES["PICHINCHA"]: {
        "name": ESTACIONES["PICHINCHA"],
        "position": (0.5, 3),
        "line": LINEAS["LINEA_E"],
    },
    ESTACIONES["ENTRE_RIOS"]: {
        "name": ESTACIONES["ENTRE_RIOS"],
        "position": (2, 3),
        "line": LINEAS["LINEA_E"],
    },
    ESTACIONES["SAN_JOSE"]: {
        "name": ESTACIONES["SAN_JOSE"],
        "position": (3, 3),
        "line": LINEAS["LINEA_E"],
    },
    ESTACIONES["INDEPENDENCIA_E"]: {
        "name": ESTACIONES["INDEPENDENCIA_E"],
        "position": (3.5, 5),
        "line": LINEAS["LINEA_E"],
    },
    ESTACIONES["BELGRANO"]: {
        "name": ESTACIONES["BELGRANO"],
        "position": (5, 7),
        "line": LINEAS["LINEA_E"],
    },
    ESTACIONES["BOLIVAR"]: {
        "name": ESTACIONES["BOLIVAR"],
        "position": (6, 8),
        "line": LINEAS["LINEA_E"],
    },
}

CONEXIONES = [
    # Línea A
    (ESTACIONES["ALBERTI"], ESTACIONES["PASCO"]),
    (ESTACIONES["PASCO"], ESTACIONES["CONGRESO"]),
    (ESTACIONES["CONGRESO"], ESTACIONES["SAENZ_PENA"]),
    (ESTACIONES["SAENZ_PENA"], ESTACIONES["LIMA"]),
    (ESTACIONES["LIMA"], ESTACIONES["PIEDRAS"]),
    (ESTACIONES["PIEDRAS"], ESTACIONES["PERU"]),
    (ESTACIONES["PERU"], ESTACIONES["PLAZA_DE_MAYO"]),
    # Línea B
    (ESTACIONES["PASTEUR"], ESTACIONES["CALLAO_B"]),
    (ESTACIONES["CALLAO_B"], ESTACIONES["URUGUAY"]),
    (ESTACIONES["URUGUAY"], ESTACIONES["CARLOS_PELLEGRINI"]),
    (ESTACIONES["CARLOS_PELLEGRINI"], ESTACIONES["FLORIDA"]),
    (ESTACIONES["FLORIDA"], ESTACIONES["LEANDRO_N_ALEM"]),
    # Línea C
    (ESTACIONES["RETIRO"], ESTACIONES["GENERAL_SAN_MARTIN"]),
    (ESTACIONES["GENERAL_SAN_MARTIN"], ESTACIONES["LAVALLE"]),
    (ESTACIONES["LAVALLE"], ESTACIONES["DIAGONAL_NORTE"]),
    (ESTACIONES["DIAGONAL_NORTE"], ESTACIONES["AVENIDA_DE_MAYO"]),
    (ESTACIONES["AVENIDA_DE_MAYO"], ESTACIONES["MORENO"]),
    (ESTACIONES["MORENO"], ESTACIONES["INDEPENDENCIA_C"]),
    (ESTACIONES["INDEPENDENCIA_C"], ESTACIONES["SAN_JUAN"]),
    (ESTACIONES["SAN_JUAN"], ESTACIONES["CONSTITUCION"]),
    # Línea D
    (ESTACIONES["FACULTAD_DE_MEDICINA"], ESTACIONES["CALLAO_D"]),
    (ESTACIONES["CALLAO_D"], ESTACIONES["TRIBUNALES"]),
    (ESTACIONES["TRIBUNALES"], ESTACIONES["9_DE_JULIO"]),
    (ESTACIONES["9_DE_JULIO"], ESTACIONES["CATEDRAL"]),
    # Línea E
    (ESTACIONES["PICHINCHA"], ESTACIONES["ENTRE_RIOS"]),
    (ESTACIONES["ENTRE_RIOS"], ESTACIONES["SAN_JOSE"]),
    (ESTACIONES["SAN_JOSE"], ESTACIONES["INDEPENDENCIA_E"]),
    (ESTACIONES["INDEPENDENCIA_E"], ESTACIONES["BELGRANO"]),
    (ESTACIONES["BELGRANO"], ESTACIONES["BOLIVAR"]),
    # Transbordos
    (ESTACIONES["BOLIVAR"], ESTACIONES["PERU"]),
    (ESTACIONES["BOLIVAR"], ESTACIONES["CATEDRAL"]),
    (ESTACIONES["CATEDRAL"], ESTACIONES["PERU"]),
    (ESTACIONES["INDEPENDENCIA_C"], ESTACIONES["INDEPENDENCIA_E"]),
    (ESTACIONES["LIMA"], ESTACIONES["AVENIDA_DE_MAYO"]),
    (ESTACIONES["DIAGONAL_NORTE"], ESTACIONES["9_DE_JULIO"]),
    (ESTACIONES["DIAGONAL_NORTE"], ESTACIONES["CARLOS_PELLEGRINI"]),
    (ESTACIONES["9_DE_JULIO"], ESTACIONES["CARLOS_PELLEGRINI"]),
]

LINEAS = {
    "LINEA_A": [
        ESTACIONES["ALBERTI"],
        ESTACIONES["PASCO"],
        ESTACIONES["CONGRESO"],
        ESTACIONES["SAENZ_PENA"],
        ESTACIONES["LIMA"],
        ESTACIONES["PIEDRAS"],
        ESTACIONES["PERU"],
        ESTACIONES["PLAZA_DE_MAYO"],
    ],
    "LINEA_B": [
        ESTACIONES["PASTEUR"],
        ESTACIONES["CALLAO_B"],
        ESTACIONES["URUGUAY"],
        ESTACIONES["CARLOS_PELLEGRINI"],
        ESTACIONES["FLORIDA"],
        ESTACIONES["LEANDRO_N_ALEM"],
    ],
    "LINEA_C": [
        ESTACIONES["RETIRO"],
        ESTACIONES["GENERAL_SAN_MARTIN"],
        ESTACIONES["LAVALLE"],
        ESTACIONES["DIAGONAL_NORTE"],
        ESTACIONES["AVENIDA_DE_MAYO"],
        ESTACIONES["MORENO"],
        ESTACIONES["INDEPENDENCIA_C"],
        ESTACIONES["SAN_JUAN"],
        ESTACIONES["CONSTITUCION"],
    ],
    "LINEA_D": [
        ESTACIONES["FACULTAD_DE_MEDICINA"],
        ESTACIONES["CALLAO_D"],
        ESTACIONES["TRIBUNALES"],
        ESTACIONES["9_DE_JULIO"],
        ESTACIONES["CATEDRAL"],
    ],
    "LINEA_E": [
        ESTACIONES["PICHINCHA"],
        ESTACIONES["ENTRE_RIOS"],
        ESTACIONES["SAN_JOSE"],
        ESTACIONES["INDEPENDENCIA_E"],
        ESTACIONES["BELGRANO"],
        ESTACIONES["BOLIVAR"],
    ],
}
