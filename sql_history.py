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
    outcome_date        DATE,
    FOREIGN KEY (animal_type_id) REFERENCES types (id),
    FOREIGN KEY (breed_id) REFERENCES breeds (id),
    FOREIGN KEY (outcome_subtypes_id) REFERENCES outcome_subtypes (id),
    FOREIGN KEY (outcome_types_id) REFERENCES outcome_types (id),
    FOREIGN KEY (color_id) REFERENCES color (id)
)
    """
    query_12 = """
    """






    query = """
                   CREATE TABLE IF NOT EXISTS animals_colors(
                   animals_id INTEGER 
                   , colors_id INTEGER
                   , FOREIGN KEY (animals_id) REFERENCES animals("index")
                   , FOREIGN KEY (colors_id) REFERENCES colors(id) 
                   ) 
    """
    # print(db_connect(query_2))

    query_3 = """
              INSERT INTO colors (color)
              SELECT DISTINCT * FROM (
                  SELECT DISTINCT 
                      color1 as color
                  FROM animals
                  UNION ALL
                  SELECT DISTINCT 
                       color2 as color
                  FROM animals
              )
    """
    # print(db_connect(query_3))

    query = """
               DELETE FROM colors WHERE color IS NULL 
    """
    # print(db_connect(query_4))

    query = """
              INSERT INTO animals_colors (animals_id, colors_id)
              SELECT DISTINCT animals."index", colors.id
              FROM animals
              INNER JOIN colors ON colors.color = animals.color1
              UNION ALL 
              SELECT DISTINCT animals."index", colors.id
              FROM animals
              INNER JOIN colors ON colors.color = animals.color2
    """
    # print(db_connect(query_5))

    query = """
              CREATE TABLE IF NOT EXISTS outcome(
                  id INTEGER PRIMARY KEY AUTOINCREMENT
                  , subtype VARCHAR (50)
                  , "type" VARCHAR (50)
                  , "month" INTEGER 
                  , "year" INTEGER
              )
                  
    """
    # print(db_connect(query_6))

    query = """
              INSERT INTO outcome (subtype, "type", "month", "year")
              SELECT DISTINCT 
                   animals.outcome_subtype
                   , animals.outcome_type
                   , animals.outcome_month
                   , animals.outcome_year
              FROM animals
    """
    # print(db_connect(query_7))

    query = """
              CREATE TABLE IF NOT EXISTS Animal_new (
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    , age_upon_outcome VARCHAR (50)
                    , animal_id VARCHAR (50)
                    , animal_type VARCHAR (50)
                    , "name" VARCHAR (50)
                    , breed VARCHAR (50)
                    , date_of_birth DATE 
                    , outcome_id INTEGER 
                    , FOREIGN KEY 
                    
              
    """


if __name__ == "__main__":
    main()
