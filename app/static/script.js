function checkSpam() {
    let message = document.getElementById("message").value;
    let result = document.getElementById("result");

    if (message.trim() === "") {
        result.innerText = "Please enter a message!";
        result.className = "";
        return;
    }

    result.innerText = "Checking...";
    result.className = "";

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        result.innerText = data.prediction;

        if (data.prediction === "SPAM") {
            result.className = "spam";       
        } else {
            result.className = "not-spam";   
        }
    })
    .catch(err => {
        result.innerText = "Error connecting to server!";
        result.className = "";
        console.error(err);
    });
}