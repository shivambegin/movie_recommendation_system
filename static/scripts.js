// Redirect to homepage if the page is refreshed
if (performance.navigation.type === 1) {
  // Check if the page is reloaded
  window.location.href = "/"; // Redirect to the homepage
}
