const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(URL, function (data) {
  const movies = data.results;
  movies.forEach((movie) => {
    const title = $('<li></li>').text(movie.title);
    $('#list_movies').append(title);
  });
});
