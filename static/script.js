// Dark Mode Toggle
const themeToggle = document.getElementById('themeToggle');
if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        themeToggle.textContent = document.body.classList.contains('dark-mode') 
            ? "☀️ Light Mode" 
            : "🌙 Dark Mode";
    });
}

// Get DOM elements
const wordList = document.getElementById("wordList");
const meaningBox = document.getElementById("meaningBox");
const alphabetButtons = document.querySelectorAll(".alphabet-btn");

// Load grouped dictionary from hidden div
const groupedDataElement = document.getElementById("groupedData");
const groupedData = JSON.parse(groupedDataElement.dataset.grouped);

// Function to show words for a selected letter
function showWords(letter) {
    wordList.innerHTML = ""; // clear previous words
    const words = groupedData[letter] || [];

    if (words.length === 0) {
        wordList.innerHTML = "<li>No words found</li>";
        return;
    }

    words.forEach(word => {
        const li = document.createElement("li");
        li.className = "word-item";
        li.textContent = word;
        li.addEventListener("click", () => loadMeaning(word));
        wordList.appendChild(li);
    });
}

// Function to fetch and display meaning
function loadMeaning(word) {
    fetch(`/get_meaning?word=${encodeURIComponent(word)}`)
        .then(res => res.json())
        .then(data => {
            meaningBox.innerHTML = `<h2>${data.word}</h2><p>${data.meaning}</p>`;
        })
        .catch(err => {
            meaningBox.innerHTML = "<p style='color:red;'>Error loading meaning 😢</p>";
            console.error(err);
        });
}

// Attach click listeners to alphabet buttons
alphabetButtons.forEach(btn => {
    btn.addEventListener("click", () => {
        const letter = btn.dataset.letter;
        showWords(letter);
    });
});
