from flask import Flask, jsonify
from sql_history import db_connect


def main():
    app = Flask(__name__)
    app.config["JSON_AS_ASCII"] = False
    app.config['DEBUG'] = True

    @app.route("/<animal_id>")
    def show_animal(animal_id):
        query = f"""
                SELECT animals_new.age_upon_outcome,
                        types."type",
                        animals_new."name",
                        color.color,
                        breeds.breed,
                        animals_new.date_of_birth,
                        outcome_subtypes.outcome_subtype,
                        outcome_types.outcome_type,
                        animals_new.outcome_month,
                        animals_new.outcome_year
                FROM animals_new
                INNER JOIN types ON animals_new.animal_type_id = types.id
                INNER JOIN breeds ON animals_new.breed_id = breeds.id
                INNER JOIN color ON animals_new.color_id  = color.id
                INNER JOIN outcome_types ON animals_new.outcome_types_id = outcome_types.id 
                LEFT JOIN outcome_subtypes ON animals_new.outcome_subtypes_id = outcome_subtypes.id
                WHERE animals_new.id == "{animal_id}"
        """
        response = db_connect(query)[0]
        response_json = {
            "age": response[0],
            "specie": response[1],
            "name": response[2],
            "color": response[3],
            "breed": response[4],
            "birthday": response[5],
            "outcome_subtype": response[6],
            "outcome_type": response[7],
            "outcome_month": response[8],
            "outcome_year": response[9]
        }
        return jsonify(response_json)

    app.run()


if __name__ == "__main__":
    main()
