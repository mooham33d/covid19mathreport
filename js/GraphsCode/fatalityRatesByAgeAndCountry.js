var MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
var color = Chart.helpers.color;
var barChartData = {
    labels: ageRanges,
    datasets: [{
        label: 'Italy',
        backgroundColor: color(window.chartColors.red).alpha(0.5).rgbString(),
        borderColor: window.chartColors.red,
        borderWidth: 1,
        data: italy
    }, {
        label: 'China',
        backgroundColor: color(window.chartColors.blue).alpha(0.5).rgbString(),
        borderColor: window.chartColors.blue,
        borderWidth: 1,
        data: china
    },{
        label: 'Netherlands',
        backgroundColor: color(window.chartColors.orange).alpha(0.5).rgbString(),
        borderColor: window.chartColors.orange,
        borderWidth: 1,
        data: netherlands
    },
    {
        label: 'South Korea',
        backgroundColor: color(window.chartColors.purple).alpha(0.5).rgbString(),
        borderColor: window.chartColors.purple,
        borderWidth: 1,
        data: SouthKorea
    },
    {
        label: 'Spain',
        backgroundColor: color(window.chartColors.green).alpha(0.5).rgbString(),
        borderColor: window.chartColors.green,
        borderWidth: 1,
        data: spain
    },

    ]

};

window.onload = function() {
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
                text: 'fatality rates'
            }
        }
    });

};