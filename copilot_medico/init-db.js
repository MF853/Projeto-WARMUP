db = db.getSiblingDB("pacientes_db");
db.pacientes_db.drop();

db.pacientes_db.insertMany([
    {
        "id": 1,
        "name": "Fulano",
        "anamnese": "Olhos vermelhos e coceira",
        "diagnostico": "dengue"
    },
    {
        "id": 2,
        "name": "Cicrano",
        "anamnese": "cancaço e dor de cabeça",
        "diagnostico": "gripe"
    },
]);