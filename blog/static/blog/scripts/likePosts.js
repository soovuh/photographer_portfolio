const likeButtons = document.querySelectorAll('.like-button');

likeButtons.forEach(button => {
    if (button.classList.contains('liked')) {
        button.disabled = true;
    }
    button.addEventListener('click', async () => {
        const postId = button.dataset.postId;

        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        };

        const response = await fetch(`/blog/like/${postId}/`, {
            method: 'POST',
            headers: headers,
        });
        const data = await response.json()
        if (data.message === 'success') {
            const postLikesElement = button.parentElement.querySelector('.like-count');
            const newLikes = parseInt(postLikesElement.textContent) + 1;
            postLikesElement.textContent = String(newLikes);
            button.disabled = true;
        }
    });
});