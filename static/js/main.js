// setTimeout(function() {
//   $('#mgalert').fadeOut('slow');
// }, 3000);
$('img.lazy').Lazy({
  // your configuration goes here
  scrollDirection: 'vertical',
  effect: 'fadeIn',
  visibleOnly: true,
  onError: function(element) {
      console.log('error loading ' + element.data('src'));
  }
});

function initMap() {
  // The location of Uluru
  const uluru = { lat: 9.9312, lng: 76.2673 };
  // The map, centered at Uluru
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 10,
    center: uluru,
  });

  // The marker, positioned at Uluru
  const marker = new google.maps.Marker({
    position: uluru,
    map: map,
  });
}