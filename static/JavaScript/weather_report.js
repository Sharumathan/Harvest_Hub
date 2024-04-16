function sendData() {
    var formData = new FormData(document.getElementById("weatherForm"));
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/weather_report", true);
    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken")); // Include CSRF token if using CSRF protection
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                // Handle successful response from server
                //console.log("Data sent successfully");
                var jsonResponse = JSON.parse(xhr.responseText);
                // Call function to update UI with JSON response
                updateWeatherInfo(jsonResponse);
                setimage(jsonResponse);
            } else {
                // Handle error response from server
                console.error("Error sending data");
            }
        }
    };
    xhr.send(formData);
}

// Function to get CSRF token from cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function updateWeatherInfo(response_data) {
    // Update DOM elements with weather data
    document.getElementById("city").innerText = "Weather In " + response_data.weather_data.city;
    document.getElementById("temperature").innerText = response_data.weather_data.temperature + " °C";
    var weatherIcon = document.getElementById("weather_report_weather-icon");
    if (weatherIcon) {
        weatherIcon.src = "http://openweathermap.org/img/wn/" + response_data.weather_data.icon + ".png";
    }
    console.log( response_data.weather_data.icon)
    //document.getElementById("weather_report_weather-icon").src = "http://openweathermap.org/img/wn/" + response_data.weather_data.icon + ".png";
    document.getElementById("description").innerText = response_data.weather_data.description;
    document.getElementById("humidity").innerText = response_data.weather_data.humidity;
    document.getElementById("pressure").innerText = response_data.weather_data.pressure;
    document.getElementById("wind-speed").innerText = response_data.weather_data.wind_speed;
    document.getElementById("wind-direction").innerText = response_data.weather_data.wind_direction;

    
}

function setimage(response_data){
    var container = document.querySelector(".weather_report");
    container.style.backgroundImage = "url('" + response_data.city_image + "')";
}

