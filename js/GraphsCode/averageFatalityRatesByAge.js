var color = Chart.helpers.color;
var barChartData = {
    labels: ageRanges,
    datasets: [{
        label: 'histogram',
        backgroundColor: color(window.chartColors.blue).alpha(0.5).rgbString(),
        // borderColor: window.chartColors.blue,
        borderWidth: 1,
        data: average,
    }, {
        label: 'line graph',
        backgroundColor: color(window.chartColors.red).alpha(0.5).rgbString(),
        borderColor: window.chartColors.red,
        borderWidth: 1,
        data: average ,
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
                text: 'average fatality rates'
            }
        }
    });

};