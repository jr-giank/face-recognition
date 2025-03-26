function triggerFileInput() {
    document.getElementById('fileInput').click();
}

function setImage(event) {
    const file = event.target.files[0];
    if (!file) {
        alert("Please select an image.");
        return;
    }

    const imageContainer = document.getElementById('imageContainer');
    const img = document.createElement('img');
    img.src = URL.createObjectURL(file);
    img.style.width = '60%';
    img.style.height = 'auto';
    imageContainer.innerHTML = '';
    imageContainer.appendChild(img);

    const imageButton = document.getElementById('imageButton');
    imageButton.style.display = "none";

}

function feedbackResponse(text, ok) {
    const feedbackContainer = document.getElementById('feedback');
    const feedbackImg = document.getElementById('feedbackImg');
    const feedbackText = document.getElementById('feedbackText');

    feedbackText.textContent = text;
    feedbackContainer.style.display = 'inline';

    if (ok) {
        feedbackContainer.style.backgroundColor = '#d8e7d0';
        feedbackImg.src = '../public/images/check.png';
        feedbackText.style.color = "#40a143";

    }
    else {
        feedbackContainer.style.backgroundColor = '#ebb6b1';
        feedbackImg.src = '../public/images/cross.png';
        feedbackText.style.color = "red";

    }
}