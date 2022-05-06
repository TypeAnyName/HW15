import sqlite3


def db_connect(query):
    with sqlite3.connect("animal.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result


def main():
    query_1 = """
                   CREATE TABLE IF NOT EXISTS types(
                   id INTEGER PRIMARY KEY AUTOINCREMENT
                   , "type" VARCHAR (50)
                   ) 
            """
    query_2 = """
                  INSERT INTO types ("type")
                  SELECT DISTINCT animal_type as "type"
                  FROM animals
                  
    """
    query_3 = """
                  CREATE TABLE IF NOT EXISTS breeds(
                  id INTEGER PRIMARY KEY AUTOINCREMENT
                  , breed VARCHAR (50)
                  )
    """
    query_4 = """
                  INSERT INTO breeds (breed)
                  SELECT DISTINCT breed as breed
                  FROM animals
    """
    query_5 = """
                 CREATE TABLE IF NOT EXISTS color(
                  id INTEGER PRIMARY KEY AUTOINCREMENT
                  , color VARCHAR (50)
                  )
    """
    query_6 = """
                  INSERT INTO color (color)
                  SELECT DISTINCT color1 as color
                  FROM animals
    """
    query_7 = """
                  CREATE TABLE IF NOT EXISTS outcome_subtypes(
                  id INTEGER PRIMARY KEY AUTOINCREMENT
                  , outcome_subtype VARCHAR (50)
                  )
    """
    query_8 = """
                  INSERT INTO outcome_subtypes (outcome_subtype)
                  SELECT DISTINCT outcome_subtype as outcome_subtype
                  FROM animals
                  WHERE outcome_subtype IS NOT NULL
    """
    query_9 = """
                  CREATE TABLE IF NOT EXISTS outcome_types(
                  id INTEGER PRIMARY KEY AUTOINCREMENT
                  , outcome_type VARCHAR (50)
                  )
    """
    query_10 = """
                  INSERT INTO outcome_types (outcome_type)
                  SELECT DISTINCT outcome_type as outcome_type
                  FROM animals
                  WHERE outcome_type IS NOT NULL
    
    """
    query_11 = """
    CREATE TABLE IF NOT EXISTS animals_new
(
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    age_upon_outcome    VARCHAR(50),
    animal_id           VARCHAR(50),
    animal_type_id      INTEGER,
    "name"              VARCHAR(50),
    color_id            INTEGER,
    breed_id            INTEGER,
    date_of_birth       DATE,
    outcome_subtypes_id INTEGER,
    outcome_types_id    INTEGER,
    outcome_month       INTEGER,
    outcome_year        INTEGER,
    FOREIGN KEY (animal_type_id) REFERENCES types (id),
    FOREIGN KEY (breed_id) REFERENCES breeds (id),
    FOREIGN KEY (outcome_subtypes_id) REFERENCES outcome_subtypes (id),
    FOREIGN KEY (outcome_types_id) REFERENCES outcome_types (id),
    FOREIGN KEY (color_id) REFERENCES color (id)
)
    """
    query_12 = """
    INSERT INTO animals_new (age_upon_outcome,
                         animal_id,
                         animal_type_id,
                         "name",
                         color_id,
                         breed_id,
                         date_of_birth,
                         outcome_subtypes_id,
                         outcome_types_id,
                         outcome_month,
                         outcome_year)
     SELECT animals.age_upon_outcome,
            animals.animal_id,
            main.types.id,
            animals.name,
            main.color.id,
            main.breeds.id,
            animals.date_of_birth,
            main.outcome_subtypes.id,
            main.outcome_types.id,
            animals.outcome_month,
            animals.outcome_year
     FROM animals
     INNER JOIN types ON types.type = animals.animal_type
     INNER JOIN color ON color.color = animals.color1
     INNER JOIN breeds ON breeds.breed = animals.breed
     LEFT JOIN outcome_subtypes ON outcome_subtypes.outcome_subtype = animals.outcome_subtype
     INNER JOIN outcome_types ON outcome_types.outcome_type = animals.outcome_type
    """


if __name__ == "__main__":
    main()
