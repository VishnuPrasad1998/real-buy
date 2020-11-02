const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
  $('#mgalert').fadeOut('slow');
}, 3000);