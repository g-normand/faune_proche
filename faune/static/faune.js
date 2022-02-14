function maPosition(position){
  var latitude = position.coords.latitude;
  var longitude = position.coords.longitude;
  $("#latitude").text(latitude);
  $("#longitude").text(longitude);
  $("#showposition").show();
  $("#errorposition").hide();
 }

function erreurPosition(error){
  var info="Erreur lors de la géolocalisation : ";
  switch(error.code) {
    case error.TIMEOUT:
    	info += "Timeout !";
    break;
    case error.PERMISSION_DENIED:
	info += "Vous n’avez pas donné la permission";
    break;
    case error.POSITION_UNAVAILABLE:
    	info += "La position n’a pu être déterminée";
    break;
    case error.UNKNOWN_ERROR:
    	info += "Erreur inconnue";
    break;
    }
  $("#errorposition").text(info);
  $("#showposition").hide();
  $("#errorposition").show();
}

$("#voir_faune").click(function(){
  var data = {};
  data['latitude'] = $('#latiude').text();
  data['longitude'] = $('#longitude').text();
  $.ajax(
    {url: "faune/geolocalise",
       data: data,
       success : function(data) {
          console.log(data);
          // window.location = data.url;
       }
    });
});

if(navigator.geolocation){
  navigator.geolocation.getCurrentPosition(maPosition, erreurPosition);
}

$(document).ready(function() {
    $("#maps_validate").on('click', function(){
        var data = {};
        data['url'] = $('#google_url').val();
        data['pas'] = '0.05';

        $.ajax(
            {url: "faune/from_google_maps",
             data: data,
             success : function(data) {
             $(".faune_info").show();
             $('#faune_url').attr('href', data.url);
             $('#faune_place').text(data.place);
             },
             error: function(data) {
               alert('Erreur lors de la récupération des données.');
             }
            });
    });

    $('#effacer').on('click', function(){
        $('#google_url').val('');
    })

});

