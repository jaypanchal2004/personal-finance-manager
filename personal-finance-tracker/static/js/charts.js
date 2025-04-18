// Initialize a basic pie chart using Chart.js
var ctx = document.getElementById('myPieChart').getContext('2d');
var myPieChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Expenses', 'Income'],
        datasets: [{
            data: [65, 35],
            backgroundColor: ['#e74c3c', '#2ecc71'],
        }]
    },
    options: {
        responsive: true
    }
});
