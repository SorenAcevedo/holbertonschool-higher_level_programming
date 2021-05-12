const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json'
$.get(URL, function (data) {
	$('#character').text(data.name);
});
