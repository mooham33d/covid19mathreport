var color = Chart.helpers.color;
var barChartData = {
    labels: ranges,
    datasets: [{
        label: 'histogram',
        backgroundColor: color(window.chartColors.blue).alpha(0.5).rgbString(),
        borderWidth: 1,
        data: ages,
    }, {
        label: 'line graph',
        backgroundColor: color(window.chartColors.red).alpha(0.5).rgbString(),
        borderColor: window.chartColors.red,
        borderWidth: 1,
        data: ages,
        type: 'line',
        fill: false,
    }]

};

window.onload = function () {
    var ctx = document.getElementById('canvas').getContext('2d');
    window.myBar = new Chart(ctx, {
        type: 'bar',
        data: barChartData,
        options: {
            responsive: true,
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'age distribution graph'
            }
        }
    });

};