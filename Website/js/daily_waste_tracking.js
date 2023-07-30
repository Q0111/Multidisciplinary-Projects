// Sample data for the graph (you can replace this with your data)
const trash_type = ['Organic', 'Plastic', 'Paper', 'Glass', 'Metal'];
const colour_template = ['red', 'yellow', 'blue', 'green', 'aqua'];

// Dữ liệu và cấu hình cho biểu đồ Bar Chart và Pie Chart
let chartData = {
  labels: trash_type,
  datasets: [{
    label: "Total Quantity",
    data: [0, 0, 0, 0, 0],
    backgroundColor: colour_template
  }]
};

// Create bar chart and pie chart for daily_waste_tracking webpage
var barChart1 = new Chart(document.getElementById('barChart1'), {
  type: 'bar',
  data: chartData
});

var pieChart1 = new Chart(document.getElementById('pieChart1'), {
  type: 'pie',
  data: chartData
});

function retrieveDataAndDisplay() {
  const url = "https://io.adafruit.com/api/v2/Group_X/feeds";

  fetch(url)
    .then(response => response.json())
    .then(data => {
      const latestData = {};

      data.forEach(item => {
        if (item.last_value !== null) {
          latestData[item.name] = item.last_value;
          delete latestData.ai_camera;
        }
      });

      // Print the latestData object to the console
      console.log(latestData);

      // Process the data and update the chart
      const dataString = latestData.daily_tracking;
      const dataPairs = dataString.split(" ");

      const updatedData = trash_type.map(trash => {
        const index = dataPairs.indexOf(trash);
        return index !== -1 ? parseInt(dataPairs[index + 1]) : 0;
      });

        chartData.datasets[0].data = updatedData;
        barChart1.update();
        pieChart1.update();
      
    })
    .catch(error => {
      console.error("Error fetching data:", error);
    });
}


// Call the retrieveDataAndDisplay() function to fetch and process the data
retrieveDataAndDisplay();
