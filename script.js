document.getElementById("generate-btn").addEventListener("click", async function () {
    const text = document.getElementById("text-input").value;
    if (text.trim() === "") {
        alert("Por favor, ingresa un resumen.");
        return;
    }

    alert("Generando video... Esto puede tardar unos segundos.");

    const response = await fetch("/generate_video", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    });

    const result = await response.json();

    if (result.video_url) {
        document.getElementById("video-preview").src = result.video_url;
        document.getElementById("download-btn").style.display = "block";
        document.getElementById("download-btn").href = result.video_url;
    } else {
        alert("Error al generar el video.");
    }
});
