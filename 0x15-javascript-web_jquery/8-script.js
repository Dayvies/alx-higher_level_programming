const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.getJSON(url, function (result) {
  $.each(result.results, function (index, item) {
    $('#list_movies').append($('<li>').text(item.title));
  });
});
