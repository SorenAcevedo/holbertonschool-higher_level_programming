$(function () {
  $('#add_item').click(function () {
    const item = $('<li></li>').text('Item');
    $('.my_list').append(item);
  });
	$('#remove_item').click(function () {
    $('li:last-child').remove();
  });
	$('#clear_list').click(function () {
    $('li').remove();
  });
});
