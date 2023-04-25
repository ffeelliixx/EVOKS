function createInput(value, id) {
    return `
    <div class="flex-shrink-0 flex-grow">
    <input type="text" name="name" id="${id}" value="${value}"
        class="shadow-sm focus:ring-gray-500 focus:border-gray-500 block w-3/4 sm:text-sm border-gray-300 rounded-md"
        >
    </div>`.trim()
}

document.getElementById("create-term-button").addEventListener("click", function(e) {
    document.getElementById("create-term-modal").classList.toggle("invisible");
});

document.getElementById("delete-term-button").addEventListener("click", function(e) {
    document.getElementById("delete-term-modal").classList.toggle("invisible");
});