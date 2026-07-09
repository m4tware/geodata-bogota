document.addEventListener('DOMContentLoaded', () => {
    const data_id = document.getElementById('chart-data');
    const chart_data = JSON.parse(data_id.textContent);

    const canva = document.getElementById('bar-chart').getContext('2d');

    new Chart(canva, {
        type: 'bar',
        data: {
        labels: chart_data['Localidad'],
        datasets: [
            {
            label: 'Hurtos 2025',
            data: chart_data['Hurtos 2025'],
            backgroundColor: 'rgba(196, 77, 86, 0.6)',
            borderColor: 'rgba(196, 77, 86, 1)',
            borderWidth: 1
            },
            {
            label: 'Llamadas 2025',
            data: chart_data['Llamadas 2025'],
            backgroundColor: 'rgba(62, 142, 172, 0.6)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
            }
        ]
        },
        options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: {
            mode: 'index',
            intersect: false
        }}
    });
});