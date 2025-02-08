document.getElementById('insuranceForm').addEventListener('submit', function (e) {
    e.preventDefault();

    // Get form values manually
    const formData = {
        age: document.getElementById('age').value,
        sex: document.getElementById('sex').value,
        bmi: document.getElementById('bmi').value,
        children: document.getElementById('children').value,
        smoker: document.getElementById('smoker').value,
        region: document.getElementById('region').value,
    };

    // Hide the form
    this.style.display = 'none';

    // Show and populate results
    const resultsSection = document.getElementById('resultsSection');
    const resultsContent = document.getElementById('resultsContent');
    resultsContent.innerHTML = ''; // Clear previous results

    // Labels for user-friendly display
    const fieldLabels = {
        age: "Age",
        sex: "Gender",
        bmi: "Body Mass Index (BMI)",
        children: "Number of Children",
        smoker: "Smoker Status",
        region: "Region",
    };

    // Create result items dynamically
    Object.entries(formData).forEach(([key, value]) => {
        const resultItem = document.createElement('div');
        resultItem.className = 'result-item';
        resultItem.innerHTML = `
            <span class="result-label">${fieldLabels[key]}:</span>
            <span class="result-value">${value}</span>
        `;
        resultsContent.appendChild(resultItem);
    });

    // Simulate model prediction score (Replace this with actual ML API call)
    const predictionScore = Math.floor(Math.random() * (95 - 75 + 1)) + 75; // Random score between 75% - 95%
    document.getElementById('predictionScore').innerText = predictionScore + "%";

    // Show results section with animation
    resultsSection.classList.add('show');
});

function newEntry() {
    // Hide results section
    document.getElementById('resultsSection').classList.remove('show');

    // Show and reset form
    const form = document.getElementById('insuranceForm');
    form.style.display = 'block';
    form.reset();

    // Reset prediction score
    document.getElementById('predictionScore').innerText = "—";
}
