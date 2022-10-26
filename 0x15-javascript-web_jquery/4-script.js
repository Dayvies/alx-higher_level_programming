#!/usr/bin/node
$('#toggle_header').click(function () {
  const color = $('header').attr('class').split(/\s+/);
  if (color[0] === 'green') $('header').removeClass('green').addClass('red');
  else $('header').removeClass('red').addClass('green');
});
