const container = document.getElementById('container');
const registerBtn = document.getElementById('Register');
const loginBtn = document.getElementById('Login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

// Event listener for the login/signup button
document.getElementById('login-btn').addEventListener('click', function() {
    // Redirect to login page
    window.location.href = 'login.html'; // Change 'login.html' to your actual login page URL if needed
});



// Function to open the Login Modal
function openLoginModal() {
    window.location.href = 'login.html';
  }
  
  // Function to close the Login Modal
  function closeLoginModal() {
    document.getElementById('loginModal').style.display = 'none';
  }
  
  // Placeholder functions for other features
  function openBookingForm() {
    alert('Trip Planning feature coming soon!');
  }
  
  function openItineraryManager() {
    alert('Itinerary Management feature coming soon!');
  }
  
  function openBookingManagement() {
    alert('Booking Management feature coming soon!');
  }
  
  function openExpenseTracker() {
    alert('Expense Tracking feature coming soon!');
  }
  
  // Close the modal when clicking outside of it
  window.onclick = function(event) {
    const modal = document.getElementById('loginModal');
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
  