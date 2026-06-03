items = []
current_id = 1

def get_all_items():
    return items

def add_item(name, value, prediction):
    global current_id
    item = {
        "id": current_id,
        "name": name,
        "value": value,
        "prediction": prediction
    }
    items.append(item)
    current_id += 1
    return item

def update_item(item_id, name, value, prediction):
    for item in items:
        if item["id"] == item_id:
            item["name"] = name
            item["value"] = value
            item["prediction"] = prediction
            return item
    return None

def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return True