var config = {
    type: 'line',
    data: {
        labels: datesOfCasesInTheWorld,
        datasets: [{
            label: 'Confirmed',
            backgroundColor: window.chartColors.blue,
            borderColor: window.chartColors.blue,
            data: confermidCasesInTheWorld,
            fill: false,
        },
        {
            label: 'Recovered',
            backgroundColor: window.chartColors.green,
            borderColor: window.chartColors.green,
            data: recoveredCasesInTheWorld,
            fill: false,
        },
        {
            label: 'Deaths',
            backgroundColor: window.chartColors.red,
            borderColor: window.chartColors.red,
            data: deadCasesInTheWorld,
            fill: false,
        },
        ]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'numper of cases in the World'
        },
        tooltips: {
            mode: 'point',
            intersect: false,
        },
        hover: {
            mode: 'nearest',
            intersect: true
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Date'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'number of cases'
                }
            }]
        }
    }
};

window.onload = function () {
    var ctx = document.getElementById('canvas').getContext('2d');
    window.myLine = new Chart(ctx, config);
};
