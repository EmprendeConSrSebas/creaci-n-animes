document.getElementById("generate-btn").addEventListener("click", async function() {
    const text = document.getElementById("input-text").value;
    
    if (text.trim() === "") {
        alert("Por favor, ingresa un texto.");
        return;
    }

    alert("Generando video...");

    const response = await fetch("http://localhost:5000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    });

    const data = await response.json();
    const videoElement = document.getElementById("output-video");
    videoElement.src = `http://localhost:5000/${data.video}`;
    videoElement.style.display = "block";

    const downloadBtn = document.getElementById("download-btn");
    downloadBtn.href = videoElement.src;
    downloadBtn.style.display = "block";
});
