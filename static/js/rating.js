/* jshint esversion: 11 */

const form = document.getElementById('rating-form');
const button = document.getElementById('submit-btn');
const loading = document.getElementById('loading');

// Reset button and hide loader
function resetRatingForm() {
    if (button) {
        button.disabled = false;
        button.textContent = 'Save Ratings';
    }
    if (loading) {
        loading.classList.add('d-none');
    }
}

if (form) {
    // Reset on page show
    window.addEventListener('pageshow', resetRatingForm);

    // Show loader and disable button on submit
    form.addEventListener('submit', () => {
        if (button) {
            button.disabled = true;
            button.textContent = 'Saving...';
        }
        if (loading) {
            loading.classList.remove('d-none');
        }
    });
}