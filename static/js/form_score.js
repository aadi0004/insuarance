document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("insuranceForm").addEventListener("submit", function (event) {
        event.preventDefault();

        let formData = new FormData(this);
        this.style.display = 'none';

        fetch("/submit_data", {
            method: "POST",
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    document.getElementById("predictionScore").innerText = "Error: " + data.error;
                } else {
                    document.getElementById("predictionScore").innerText = "Predicted Insurance Cost: " + data.prediction;
                }
                document.getElementById("resultsSection").style.display = "block";
            })
            .catch(error => {
                console.error("Error:", error);
            });
    });
});

function newEntry() {
    document.getElementById("insuranceForm").reset();
    document.getElementById("insuranceForm").style.display = "block";
    document.getElementById("resultsSection").style.display = "none";
    document.getElementById("predictionScore").innerText = "—";
}