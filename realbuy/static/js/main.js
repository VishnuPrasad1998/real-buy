setTimeout(function() {
  $('#msgalert').fadeOut('slow');
}, 3000);

function initMap() {
  // The location of Uluru
  const uluru = { lat: 9.9312, lng: 76.2673 };
  // The map, centered at Uluru
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 15,
    center: uluru,
  });

  // The marker, positioned at Uluru
  const marker = new google.maps.Marker({
    position: uluru,
    map: map,
  });
}