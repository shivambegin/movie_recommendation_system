async function searchMovies() {
    const query = document.getElementById('searchInput').value;

    if (!query) {
        alert("Please enter a movie name");
        return;
    }

    const response = await fetch(`/search?query=${query}`);
    const movies = await response.json();

    const movieList = document.getElementById('movieList');
    movieList.innerHTML = '';

    if (movies.length === 0) {
        movieList.innerHTML = "<p>No movies found.</p>";
        return;
    }

    movies.forEach(movie => {
        const movieCard = document.createElement('div');
        movieCard.innerHTML = `
            <h3>${movie.title}</h3>
            <p>Genre: ${movie.genre}</p>
            <p>Rating: ${movie.rating}</p>
            <img src="${movie.poster}" alt="${movie.title}">
        `;
        movieList.appendChild(movieCard);
    });
}