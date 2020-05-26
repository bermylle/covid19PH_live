// [Data Set A]
// Line graph 
var config = {
   options: {
    title: {
      display: true,
      text: 'COVID19 Cases in the Philippines'
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
        //type: "line",
        data: ph_confirmed,
        label: 'Confirmed Cases',
        borderColor: "#c45850",
        fill: false
      }, { 
        //type: "line",
        data: ph_recoveries,
        label: 'Recoveries',
        borderColor: "#3cba9f",
        fill: false
      }, { 
        //type: "line",
        data: ph_deaths,
        label: 'Deaths',
        borderColor: "#e8c3b9",
        fill: false
      }
    ]
  }
};
var ctx = document.getElementById("line-chart-ph");
var chart = new Chart(ctx, config);


