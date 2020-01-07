// used to send POST requests
var xhttp = new XMLHttpRequest();

// get the crsf token from cookie
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}


// Grab all the squares
var squares = document.querySelectorAll("td");

// Clear Squares Function
function clearBoard() {
  for (var i = 0; i < squares.length; i++) {
      squares[i].textContent = '';
  }
}

// Create a function that will check the square marker
function changeMarker(){
  // send a POST request with the position clicked
  var csrftoken = getCookie('csrftoken');
  alert(csrftoken);
  xhttp.open("POST", "", true);
  xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhttp.setRequestHeader("X-CSRFToken", csrftoken);
  xhttp.send("csrfmiddlewaretoken="+csrftoken+"&id="+this.id);
  //xhttp.send(this.id);
  if(this.textContent === ''){
    this.textContent = 'X';
  }
};

// Use a for loop to add Event listeners to all the squares
for (var i = 0; i < squares.length; i++) {
    squares[i].addEventListener('click', changeMarker);
}
