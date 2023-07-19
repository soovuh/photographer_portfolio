const createBtn = document.querySelector('.create');
const createReviewForm = document.querySelector('.center-screen');
const createReviewFormBlock = document.querySelector('.review-form');
const closeIcon = document.querySelector('.close-icon');
createBtn.addEventListener('click', () => {
    createReviewForm.classList.add('show');
})

document.addEventListener("click", (event) => {
    if (!createReviewFormBlock.contains(event.target) && !createBtn.contains(event.target) || closeIcon.contains(event.target)) {
        createReviewForm.classList.remove('show');
    }
});