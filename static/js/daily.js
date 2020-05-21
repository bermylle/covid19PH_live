// [Data Set A]
// Line graph 
var config = {
   options: {
    title: {
      display: true,
      text: 'Daily confirmed cases in the Philippines'
    },
    scales: {
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
        borderColor: "#c45850",
        backgroundColor: "#ffffff",
        hoverBackgroundColor: "#cceabb", 
        lineTension: 0.3,

        fill: false,
      }
    ]
  }
};
var ctx = document.getElementById("line-chart-daily");
var chart = new Chart(ctx, config);