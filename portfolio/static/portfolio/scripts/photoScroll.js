function getElementsArray() {
    const firstColumnDivs = document.querySelector('.first').querySelectorAll('.photo_link');
    const secondColumnDivs = document.querySelector('.second').querySelectorAll('.photo_link');

    const combinedArray = []

    const minLength = Math.min(firstColumnDivs.length, secondColumnDivs.length);
    const maxLength = Math.max(firstColumnDivs.length, secondColumnDivs.length);

    for (let i = 0; i < minLength; i++) {
        combinedArray.push(firstColumnDivs[i]);
        combinedArray.push(secondColumnDivs[i]);
    }

    if (maxLength - minLength === 1) {
        combinedArray.push(firstColumnDivs[minLength] || secondColumnDivs[minLength]);
    }

    return combinedArray
}

const staticBody = document.querySelector('body')
const photoLinks = getElementsArray();
const fullscreenContainer = document.querySelector('.fullscreen-container');
const fullscreenImage = document.querySelector('.fullscreen-image');
const fullscreenClose = document.querySelector('.fullscreen-close');
const fullscreenArrows = document.querySelector('.fullscreen-arrows');
const fullscreenArrowBack = document.querySelector('.fullscreen-arrow[name="chevron-back"]');
const fullscreenArrowForward = document.querySelector('.fullscreen-arrow[name="chevron-forward"]');
let currentPhotoIndex = 0;

function showFullscreenPhoto(index) {
    fullscreenImage.src = photoLinks[index].querySelector('img').src;
    staticBody.classList.add('static')
    fullscreenContainer.classList.add('show');
    fullscreenImage.classList.add('fade_in');
}

function hideFullscreenPhoto() {
    fullscreenContainer.classList.remove('show');
    staticBody.classList.remove('static');
    fullscreenImage.classList.remove('fade_in');
}

photoLinks.forEach((link, index) => {
    link.addEventListener('click', () => {
        showFullscreenPhoto(index);
    });
});

fullscreenClose.addEventListener('click', () => {
    hideFullscreenPhoto();
});

fullscreenArrowBack.addEventListener('click', () => {
    currentPhotoIndex = (currentPhotoIndex - 1 + photoLinks.length) % photoLinks.length;
    fullscreenImage.classList.remove('fade_in')
    setTimeout(() => {
        showFullscreenPhoto(currentPhotoIndex);
    }, 150);

});

fullscreenArrowForward.addEventListener('click', () => {
    currentPhotoIndex = (currentPhotoIndex + 1) % photoLinks.length;
    fullscreenImage.classList.remove('fade_in')
    setTimeout(() => {
        showFullscreenPhoto(currentPhotoIndex);
    }, 150);
});