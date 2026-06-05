import json
import os

DATA_FILE = "data.json"


def load_items():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump([], file)

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_items(items):
    with open(DATA_FILE, "w") as file:
        json.dump(items, file, indent=4)


def get_all_items():
    return load_items()


def add_item(name, value, prediction):
    items = load_items()

    new_id = 1
    if items:
        new_id = max(item["id"] for item in items) + 1

    item = {
        "id": new_id,
        "name": name,
        "value": value,
        "prediction": prediction
    }

    items.append(item)
    save_items(items)

    return item


def update_item(item_id, name, value, prediction):
    items = load_items()

    for item in items:
        if item["id"] == item_id:
            item["name"] = name
            item["value"] = value
            item["prediction"] = prediction

            save_items(items)
            return item

    return None


def delete_item(item_id):
    items = load_items()

    items = [item for item in items if item["id"] != item_id]

    save_items(items)

    return True