const API_URL = "/api/items";

window.onload = loadItems;

// LOAD ITEMS
function loadItems() {
    fetch(API_URL)
        .then(res => res.json())
        .then(data => {
            let rows = "";

            data.forEach(item => {
                rows += `
                    <tr>
                        <td>${item.id}</td>
                        <td>${item.name}</td>
                        <td>${item.value}</td>
                        <td>${item.prediction}</td>
                        <td>
                            <button class="edit-btn" onclick="editItem(${item.id}, '${item.name}', ${item.value})">Edit</button>
                            <button class="delete-btn" onclick="deleteItem(${item.id})">Delete</button>
                        </td>
                    </tr>
                `;
            });

            document.getElementById("tableData").innerHTML = rows;
        });
}

// ADD ITEM
function addItem() {
    const name = document.getElementById("name").value;
    const value = document.getElementById("value").value;

    if (!name || !value) {
        alert("Please enter all fields");
        return;
    }

    fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, value })
    })
    .then(res => res.json())
    .then(() => {
        clearForm();
        loadItems();
    });
}

// EDIT (fill form)
function editItem(id, name, value) {
    document.getElementById("itemId").value = id;
    document.getElementById("name").value = name;
    document.getElementById("value").value = value;
}

// UPDATE ITEM (FIXED)
function updateItem() {
    const id = document.getElementById("itemId").value;
    const name = document.getElementById("name").value;
    const value = document.getElementById("value").value;

    if (!id) {
        alert("Please click Edit first");
        return;
    }

    fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, value })
    })
    .then(res => res.json())
    .then(() => {
        clearForm();
        loadItems();
    });
}

// DELETE
function deleteItem(id) {
    fetch(`${API_URL}/${id}`, {
        method: "DELETE"
    })
    .then(() => loadItems());
}

// CLEAR FORM
function clearForm() {
    document.getElementById("itemId").value = "";
    document.getElementById("name").value = "";
    document.getElementById("value").value = "";
}