// Sample data for the graph (you can replace this with your data)
const day = ["Mon", "Tue", "Thur", "Wed", "Fri", "Sat", "Sun"];
let organicData = [];
let plasticData = [];
let paperData = [];
let glassData = [];
let metalData = [];
let totalData = [];

// Function to draw the graph using Chart.js
function drawGraph(chartID, database, title) {
  const ctx = document.getElementById(chartID).getContext('2d');

  // Split the database array into two datasets
  let firstSevenData = database.slice(0, 7);
  let lastValue = database[database.length - 1];

  // Create a new array with the repeated last value for the last dataset
  let lastData = Array(day.length - 1).fill(lastValue);
  lastData.push(lastValue);

  const myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: day,
      datasets: [
        {
          label: 'Daily Amount',
          data: firstSevenData,
          borderColor: 'rgb(75, 192, 192)',
          borderWidth: 3,
          fill: false,
        },
        {
          label: 'Average',
          data: lastData,
          borderColor: 'rgb(255, 99, 132)',
          borderWidth: 3,
          fill: false,
        },
      ],
    },
    options: {
      plugins: {
        title: {
          display: true,
          text: title,
          padding: {
            top: 10,
            bottom: 30
          },
          font: {
            size: 20
          }
        }
      },
      scales: {
        x: {
          ticks: {
            font: {
              size: 15
            }
          }
        },
        y: {
          title: {
            display: true,
            text: 'Amount(Kg)'
          },
          ticks: {
            font: {
              size: 15 
            }
          }
        }
      },
    },
  });
}

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

      // Assign the weekly_tracking data to the followed array
      for (let prop in latestData) {
        // Split the value of the current property using space or comma as the separator
        let values = latestData[prop].split(/[ ,]+/);
      
        // Convert the split values to numbers using parseInt() or parseFloat()
        let numericValues = values.map(val => parseInt(val)); // Use parseFloat() for floating-point numbers
      
        // Update the corresponding array based on the property name
        if (prop === "organic_week") {
          organicData = numericValues;
        } else if (prop === "plastic_week") {
          plasticData = numericValues;
        } else if (prop === "paper_week") {
          paperData = numericValues;
        } else if (prop === "glass_week") {
          glassData = numericValues;
        } else if (prop === "metal_week") {
          metalData = numericValues;
        } else {
          totalData = numericValues;
        }
      }

      // After the data has been fetched and processed, draw the graphs
      drawGraph('myChart1', organicData, "Organic");
      drawGraph('myChart2', plasticData, "Plastic");
      drawGraph('myChart3', paperData, "Paper");
      drawGraph('myChart4', glassData, "Glass");
      drawGraph('myChart5', metalData, "Metal");
      drawGraph('myChart6', totalData, "Total Quantity");
    })
    .catch(error => {
      console.error("Error fetching data:", error);
    });
}

retrieveDataAndDisplay();

let mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}