
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
    labels: ph_dates,
    datasets: [{ 
        data: daily_count,
        label: 'Confirmed Cases',
        borderColor: "#0a97b0",
        backgroundColor: "white",
        lineTension: 0.3,

        fill: false,
      }
    ]
  }
});

