function onClickedPredictDelay() {
    console.log("Estimate delay button clicked");
    var MONTH = document.getElementById("uimonth");
    var DAY = document.getElementById("uiday");
    var DAY_OF_WEEK = document.getElementById("uiday_of_week");
    var SCHEDULED_DEPARTURE = document.getElementById("uischeduled_departure")
    var DEPARTURE_TIME = document.getElementById("uideparture_time") 
    var DEPARTURE_DELAY = document.getElementById("uideparture_delay");
    var TAXI_OUT = document.getElementById("uitaxi_out");
    var SCHEDULED_ARRIVAL= document.getElementById("uischeduled_arrival");
    var AIRLINE = document.getElementById("uiAIRLINE");
    var ORIGIN_AIRPORT = document.getElementById("uiORIGIN_AIRPORT");
    var DESTINATION_AIRPORT = document.getElementById("uiDESTINATION_AIRPORT");
    var ESTDELAY = document.getElementById("uiPredictdelay");

   var url = "http://127.0.0.1:5000/predict_delay"; //Use this if you are NOT using nginx which is first 7 tutorials
   //var url = "/api/predict_flight_delay"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
    MONTH: parseInt(MONTH.value),
    DAY: parseInt(DAY.value),
    DAY_OF_WEEK: parseInt(DAY_OF_WEEK.value),
    SCHEDULED_DEPARTURE: parseFloat(SCHEDULED_DEPARTURE.value),
    DEPARTURE_TIME: parseFloat(DEPARTURE_TIME.value),
    DEPARTURE_DELAY : parseFloat(DEPARTURE_DELAY.value),
    TAXI_OUT: parseFloat(TAXI_OUT.value),
    SCHEDULED_ARRIVAL: parseFloat( SCHEDULED_ARRIVAL.value),
      AIRLINE: AIRLINE.value,
      ORIGIN_AIRPORT: ORIGIN_AIRPORT.value,
      DESTINATION_AIRPORT: DESTINATION_AIRPORT.value
  },function(data, status) {
      console.log(data.estimated_delay);
      ESTDELAY.innerHTML = "<h2>" + data.estimated_delay.toString() + " MINUTES</h2>";
      console.log(status);
  });
}

function onPageLoad() {
    console.log( "document loaded" );
     var url = "http://127.0.0.1:5000/get_airline_names"; // Use this if you are NOT using nginx which is first 7 tutorials
     //var url = "/api/get_airline_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_airline_names request");
        if(data) {
            var AIRLINE= data.airlines;
            var uiAIRLINE = document.getElementById("uiAIRLINE");
            $('#uiAIRLINE').empty();
            for(var i in AIRLINE) {
                var opt = new Option(AIRLINE[i]);
                $('#uiAIRLINE').append(opt);
            }
        }
    });
  }
  
  
   {
    console.log( "document loaded" );
     var url = "http://127.0.0.1:5000/get_origin_names"; // Use this if you are NOT using nginx which is first 7 tutorials
     //var url = "/api/get_origin_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_origin_names request");
        if(data) {
            var ORIGIN_AIRPORT= data.origin;
            var uiORIGIN_AIRPORT = document.getElementById("uiORIGIN_AIRPORT");
            $('#uiORIGIN_AIRPORT').empty();
            for(var i in ORIGIN_AIRPORT) {
                var opt = new Option(ORIGIN_AIRPORT[i]);
                $('#uiORIGIN_AIRPORT').append(opt);
            }
        }
    });
  }
  
   {
    console.log( "document loaded" );
     var url = "http://127.0.0.1:5000/get_destination_names"; // Use this if you are NOT using nginx which is first 7 tutorials
     //var url = "/api/get_destination_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_destination_names request");
        if(data) {
            var DESTINATION_AIRPORT= data.destination;
            var uiDESTINATION_AIRPORT = document.getElementById("uiDESTINATION_AIRPORT");
            $('#uiDESTINATION_AIRPORT').empty();
            for(var i in DESTINATION_AIRPORT) {
                var opt = new Option(DESTINATION_AIRPORT[i]);
                $('#uiDESTINATION_AIRPORT').append(opt);
            }
        }
    });
  }

  window.onload = onPageLoad;