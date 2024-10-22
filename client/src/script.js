const container = document.getElementById('container');
const registerBtn = document.getElementById('Register');
const loginBtn = document.getElementById('Login');
const homeBtn = document.getElementById('Home');
const flightBtn = document.getElementById('Flight');
const trainBtn = document.getElementById('Train');
const busBtn = document.getElementById('Bus');
const itineraryBtn = document.getElementById('Itinerary');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

homeBtn.addEventListener('click', () => {
  container.classList.remove("active");
});

flightBtn.addEventListener('click', () => {
  container.classList.remove("active");
});

trainBtn.addEventListener('click', () => {
  container.classList.remove("active");
});

busBtn.addEventListener('click', () => {
  container.classList.remove("active");
});

itineraryBtn.addEventListener('click', () => {
  container.classList.remove("active");
});

// Event listener for the login/signup button
document.getElementById('Login').addEventListener('click', function() {
    // Redirect to login page
    window.location.href = 'login.html'; // Change 'login.html' to your actual login page URL if needed
});

document.getElementById('Home').addEventListener('click', function() {
  window.location.href = 'homepage.html';
})

document.getElementById('Flight').addEventListener('click', function() {
  window.location.href = 'flights.html';
})

document.getElementById('Train').addEventListener('click', function() {
  window.location.href = 'trains.html';
})

document.getElementById('Bus').addEventListener('click', function() {
  window.location.href = 'buses.html';
})

document.getElementById('Itinerary').addEventListener('click', function() {
  window.location.href = 'Itenary.html';
})

document.addEventListener('DOMContentLoaded', function () {
  console.log("Script is loaded!"); // Debugging message

  const flightsButton = document.getElementById('Flight');
  if (flightsButton) {
      console.log("Flights button found!"); // Debugging message
      flightsButton.addEventListener('click', function () {
          console.log("Flights button clicked!"); // Debugging message
          window.location.href = 'flights.html'; // Ensure flights.html exists
      });
  }

  const trainsButton = document.getElementById('Train');
  if (trainsButton) {
      console.log("Trains button found!"); // Debugging message
      trainsButton.addEventListener('click', function () {
          console.log("Trains button clicked!"); // Debugging message
          window.location.href = 'trains.html'; // Ensure trains.html exists
      });
  }

  const itineraryButton = document.getElementById('Itinerary');
  if (itineraryButton) {
      console.log("Itinerary button found!"); // Debugging message
      itineraryButton.addEventListener('click', function () {
          console.log("Itinerary button clicked!"); // Debugging message
          window.location.href = 'itinerary.html'; // Ensure itinerary.html exists
      });
  }

  const loginButton = document.querySelector('.login-button');
  if (loginButton) {
      console.log("Login button found!"); // Debugging message
      loginButton.addEventListener('click', function () {
          console.log("Login button clicked!"); // Debugging message
          window.location.href = 'login.html'; // Ensure login.html exists
      });
  }

  const homeButton = document.getElementById('Home');
  if (homeButton) {
      console.log("Home button found!"); // Debugging message
      homeButton.addEventListener('click', function () {
          console.log("Home button clicked!"); // Debugging message
          window.location.href = 'homepage.html'; // Ensure homepage.html exists
      });
  }
});

