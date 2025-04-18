// Example JavaScript function for handling form submission
function submitForm() {
    const formData = new FormData(document.getElementById('form-id'));
    fetch('/submit', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        alert('Form Submitted!');
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
