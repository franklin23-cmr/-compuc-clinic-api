from shared.serializer import enum_serializer

TYPES_PARAMETRE = (
    ('Taille', 'Taille'),
    ('Poids', 'Poids'),
    ('Température', 'Température'),
    ('Pression', 'Pression Sanguine'),
)

TYPES_SYMPTOME = (
    ('A', 'A'),
    ('B', 'B')
)

TYPE = (
        (0, 'Consultation'),
        (1, 'Suivi')
    )

LISTE_ENUM = {
    'TYPE_PARAMETRE': enum_serializer(TYPES_PARAMETRE),
    'TYPES_SYMPTOME': enum_serializer(TYPES_SYMPTOME),
    'TYPE': enum_serializer(TYPE),
}