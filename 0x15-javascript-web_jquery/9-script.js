const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(URL, function (data) {
  $('#hello').text(data.hello);
});
