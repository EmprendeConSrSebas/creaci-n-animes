document.getElementById("generate-btn").addEventListener("click", async function () {
    const text = document.getElementById("text-input").value;
    if (text.trim() === "") {
        alert("Por favor, ingresa un resumen.");
        return;
    }

    // Simulación de generación rápida del video
    alert("Generando video... Esto puede tardar unos segundos.");

    // Aquí podríamos integrar IA para generar imágenes y voz
    // Por ahora, simulamos un video con un clip predefinido
    setTimeout(() => {
        document.getElementById("video-preview").src = "https://www.w3schools.com/html/mov_bbb.mp4"; // Video de prueba
        document.getElementById("download-btn").style.display = "block";
        document.getElementById("download-btn").href = "https://www.w3schools.com/html/mov_bbb.mp4"; // Enlace de prueba
    }, 3000);
});
