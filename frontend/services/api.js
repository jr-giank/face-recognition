const fetchPath = "http://127.0.0.1:8000";

async function uploadImage() {

    const fileInput = document.getElementById('fileInput');
    if (!fileInput.files.length) {
        alert('Please select an image');
        return;
    }

    const formData = new FormData();
    formData.append("name", fileInput.files[0].name);
    formData.append("image", fileInput.files[0]);

    try {
        const response = await fetch(fetchPath + "/api/upload-image/", {
            method: "POST",
            body: formData
        });


        const result = await response.json();
        if(response.ok)
        {
            feedbackResponse("Carga Exitosa", true);
            
        }
        else{
            feedbackResponse("Error en Carga", false);

        }


    } catch (error) {
        console.log(error)

    }
}

async function compareFace() {
    const fileInput = document.getElementById('fileInput');
    if (!fileInput.files.length) {
        alert('Please select an image');
        return;
    }

    const formData = new FormData();
    formData.append("image", fileInput.files[0]);

    try {
        const response = await fetch(fetchPath + "/api/compare-faces/", {
            method: "POST",
            body: formData
        });

        const result = await response.json();
        if(response.ok)
        {
            feedbackResponse("Rostro Encontrado", true);
            const nombre = document.getElementById('name');
            const imageName = result.data.name.split('.').slice(0, -1).join('.');
            nombre.innerHTML = imageName;
            
        }
        else{
            feedbackResponse("Rostro No Encontrado", false);

        }


    } catch (error) {
        console.log(error)

    }
}