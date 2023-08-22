function initMap() {
    const myLatLng = { lat: 52.66568422490566, lng: 0.1604611599127387 };
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 17,
        center: myLatLng,
    });

    new google.maps.Marker({
        position: myLatLng,
        map,
    });
}
