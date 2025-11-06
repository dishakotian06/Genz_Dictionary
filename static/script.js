

const themeToggle = document.getElementById('themeToggle');
themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    themeToggle.textContent = document.body.classList.contains('dark-mode') ? '☀️ Light Mode' : '🌙 Dark Mode';
});


document.querySelectorAll('.floating-emojis span').forEach(span => {
    span.style.setProperty('--random-top', Math.random());
    span.style.setProperty('--random-left', Math.random());
});





