import json
import os
from flask import Blueprint, jsonify, request

notes_bp = Blueprint("notes", __name__)

DATA_FILE = "data/notes.json"


def load_notes():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_notes(notes):
    with open(DATA_FILE, "w") as file:
        json.dump(notes, file, indent=4)


@notes_bp.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(load_notes())


@notes_bp.route("/notes", methods=["POST"])
def create_note():
    notes = load_notes()

    data = request.get_json()

    if not data or "title" not in data or "content" not in data:
        return jsonify({"error": "title and content are required"}), 400

    note = {
        "id": len(notes) + 1,
        "title": data["title"],
        "content": data["content"]
    }

    notes.append(note)
    save_notes(notes)

    return jsonify(note), 201


@notes_bp.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    notes = load_notes()

    data = request.get_json()

    for note in notes:
        if note["id"] == note_id:
            note["title"] = data.get("title", note["title"])
            note["content"] = data.get("content", note["content"])

            save_notes(notes)
            return jsonify(note)

    return jsonify({"error": "Note not found"}), 404


@notes_bp.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    notes = load_notes()

    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            return jsonify({"message": "Note deleted"})

    return jsonify({"error": "Note not found"}), 404