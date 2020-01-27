from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

import models
# set animals to to be a blueprint that will be named animals and be imported as animals
animals = Blueprint('animals', 'animals')

#index
@animals.route('/', methods=["GET"])
def get_all_animals():
    try:
        animals = [model_to_dict(animal) for animal in models.Animal.select()]
        print(animals)
        return jsonify(data=animals, status={"code": 200, "message": "success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code":400, "message": "Error getting resoures"})

# Create route
@animals.route('/', methods=["POST"])
def create_animal():
    try:
        payload = request.get_json()
        animal = models.Animal.create(**payload)
        print(animal.__dict__)
        animal_dict = model_to_dict(animal)

        return jsonify(data = animal_dict, status = {"code": 201, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error creating the resources"})

# Show route
@animals.route('/<id>', methods=["GET"])
def get_one_animal(id):
    try:
        animal = models.Animal.get_by_id(id)
        print(animal)
        animal_dict = model_to_dict(animal)
        return jsonify(data = animal_dict, status={"code": 200, "message": f"Found animal with id {animal.id}"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error getting one resource"})

# Update route
@animals.route('/<id>', methods=["PUT"])    
def update_animal(id):
    try:
        payload = request.get_json()
        query = models.Animal.update(**payload).where(models.Animal.id == id)
        query.execute()
        updated_animal = model_to_dict(models.Animal.get_by_id(id))
        return jsonify(data=updated_animal, status={"code": 200, "message": f"Resourced updated successfully"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error updating one resource"})


# Delete route
@animals.route('/<id>', methods=["DELETE"])
def delete_animal(id):
    try:
        query = models.Animal.delete().where(models.Animal.id == id)
        query.execute()
        return jsonify(data='Resource successfully deleted', status={"code": 200, "message": "Resource successfully deleted"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error deleting resource"})