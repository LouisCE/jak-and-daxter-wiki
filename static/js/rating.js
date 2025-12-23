document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('rating-form');
    if (!form) return;

    form.addEventListener('submit', () => {
        const button = document.getElementById('submit-btn');
        const loading = document.getElementById('loading');

        if (button) button.disabled = true;
        if (loading) loading.classList.remove('d-none');
    });
});