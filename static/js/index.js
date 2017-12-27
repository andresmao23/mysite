$( document ).ready(function(){
    $(".button-collapse").sideNav();
    $('.slider').slider();

    $('.fixed-action-btn').openFAB();
    $('.fixed-action-btn').closeFAB();
    $('.fixed-action-btn.toolbar').openToolbar();
    $('.fixed-action-btn.toolbar').closeToolbar();

    $('.materialboxed').materialbox();

})

function initMap() {
    var popayan = {lat: 2.459526, lng: -76.594710};
    var casa = {lat: 2.460946, lng: -76.591674};
    var parque_caldas = {lat: 2.442238, lng: -76.606349};
    var mapOptions = {zoom: 13, center: popayan}

    var map = new google.maps.Map(document.getElementById('map'), mapOptions); 
    var marker = new google.maps.Marker({
        position: popayan,
        title: 'Centro comercial Campanario'
    });
    var marker_casa = new google.maps.Marker({
        position: casa,
        title: 'Yo :)'
    });
    var marker_parque_caldas = new google.maps.Marker({
        position: parque_caldas,
        title: 'Parque Caldas'
    });
    marker.setMap(map);
    marker_casa.setMap(map);
    marker_parque_caldas.setMap(map);
}