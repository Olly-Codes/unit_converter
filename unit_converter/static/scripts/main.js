const categoryButtons = document.querySelectorAll(".category-btn");
const hiddenCategoryInput = document.querySelector("#category");
const fromUnit = document.querySelector("#from_unit");
const toUnit = document.querySelector("#to_unit");

const unitOptions = {
    length: ['mm','cm', 'm', 'km', 'inch', 'foot', 'yard', 'mile'],
    weight: ['mg', 'g', 'kg', 'ounces', 'pounds'],
    temperature: ['C', 'F', 'K']
};

let updateDropdowns = (category) => {
    fromUnit.innerHTML = ''
    toUnit.innerHTML = ''

    unitOptions[category].forEach(unit => {
        let option1 = new Option(unit, unit);
        let option2 = new Option(unit, unit);

        fromUnit.add(option1);
        toUnit.add(option2);
    });
}

categoryButtons.forEach(button => {
    button.addEventListener('click', () => {
        let selectedCategory = button.getAttribute("data-category");
        hiddenCategoryInput.value = selectedCategory;

        categoryButtons.forEach(btn => btn.classList.remove("active"));
        button.classList.add("active")

        updateDropdowns(selectedCategory)
    });
});

updateDropdowns(hiddenCategoryInput.value);