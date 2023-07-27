const renderChart = (data, labels) => {
    var ctx = document.getElementById("myChart").getContext("2d");
    var myChart = new Chart(ctx, {
      type: "bar",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Last 3 months income",
            data: data,
            backgroundColor: [
              "rgba(75, 192, 192, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(201, 203, 207, 0.2)",
              "rgba(255, 159, 64, 0.2)",
            ],
            borderColor: [
              "rgb(75, 192, 192,1)",
              "rgba(54, 162, 235, 1)",
              'rgb(153, 102, 255,1)',
              "rgba(75, 192, 192, 1)",
              "rgba(201,203,207,1)",
              "rgba(255, 159, 64, 1)",
            ],
            borderWidth: 1,
          },
        ],
      },
      options: {
        title: {
          display: true,
          text: "Income per source",
        },
      },
    });
  };
  
  const getChartData = () => {
    console.log("fetching");
    fetch("/income/income_source_summary")
      .then((res) => res.json())
      .then((results) => {
        console.log("results", results);
        const source_data = results.income_source_data;
        const [labels, data] = [
          Object.keys(source_data),
          Object.values(source_data),
        ];
  
        renderChart(data, labels);
      });
  };
  
  window.onload = getChartData();