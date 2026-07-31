let allBooks = [];
const table = document.querySelector('#book-table');

fetch('books.json')
    .then(response => response.json())
    .then(data => {
        allBooks = data;
        renderTable('score');
    });

function renderTable(sortBy) {
    let sorted = [...allBooks];

    if (sortBy === 'score') {
        sorted.sort((a, b) => b.score - a.score);
    } else if (sortBy === 'rating') {
        sorted.sort((a, b) => b.rating - a.rating);
    } else if (sortBy === 'price') {
        sorted.sort((a, b) => a.price - b.price);
    }

    const rows = table.querySelectorAll('tr:not(:first-child)');
    rows.forEach(row => row.remove());

    sorted.forEach((book, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${index + 1}</td>
            <td>${book.title}</td>
            <td>£${book.price}</td>
            <td>${book.rating}</td>
            <td>${book.score.toFixed(2)}</td>
        `;
        table.appendChild(row);
    });
}