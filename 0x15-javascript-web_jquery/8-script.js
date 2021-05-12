const URL = 'https://swapi-api.hbtn.io/api/films/?format=json'
$.get(URL, function (data) {
	let movies = data.results;
	movies.forEach((movie) => {
		let title = $('<li></li>').text(movie.title);
		$('#list_movies').append(title);
	});
});
