
// [Data Set A]
// Line graph 

var ctx = document.getElementById("line-chart-daily");
var line = new Chart(ctx, {
   options: {
/*    title: {
      display: true,
      text: 'Daily confirmed cases in the Philippines'
    },
*/    scales: {
        yAxes: [{
            display: true,
            ticks: {
            }
        }]
    }
  },
  type: 'line',
  data: {
    labels: ph_dates_daily,
    datasets: [{ 
        data: daily_count,
        label: 'Confirmed Cases',
        borderColor: "#ffa34d",
        backgroundColor: "#a0204c",
        lineTension: 0.4,

        fill: false,
      }
    ]
  }
});

