// Sample data for the graph (you can replace this with your data)
const x1Data = [1, 2, 3, 4, 5];
const y1Data = [10, 60, 15, 30, 25];

// Function to draw the graph using Chart.js
function drawGraph1() {
  const ctx = document.getElementById('myChart1').getContext('2d');
  const myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: x1Data,
      datasets: [{
        label: 'Total Quantity',
        data: y1Data,
        borderColor: 'rgb(75, 192, 192)',
        borderWidth: 2,
        fill: false,
      }]
    },
    options: {
      scales: {
        x: {
          title: {
            display: true,
            text: 'Time'
          }
        },
        y: {
          title: {
            display: true,
            text: 'Amount'
          }
        }
      }
    }
  });
}

// Sample data for the graph (you can replace this with your data)
const x2Data = [1, 2, 3, 4, 5];
const y2Data = [30, 40, 15, 30, 25];

// Function to draw the graph using Chart.js
function drawGraph2() {
  const ctx = document.getElementById('myChart2').getContext('2d');
  const myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: x2Data,
      datasets: [{
        label: 'Organic waste',
        data: y2Data,
        borderColor: 'rgb(75, 192, 192)',
        borderWidth: 2,
        fill: false,
      }]
    },
    options: {
      scales: {
        x: {
          title: {
            display: true,
            text: 'Time'
          }
        },
        y: {
          title: {
            display: true,
            text: 'Y-axis Label'
          }
        }
      }
    }
  });
}

// Sample data for the graph (you can replace this with your data)
const x3Data = [1, 2, 3, 4, 5];
const y3Data = [10, 60, 15, 30, 25];

// Function to draw the graph using Chart.js
function drawGraph3() {
  const ctx = document.getElementById('myChart3').getContext('2d');
  const myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: x3Data,
      datasets: [{
        label: 'Paper Waste',
        data: y3Data,
        borderColor: 'rgb(75, 192, 192)',
        borderWidth: 2,
        fill: false,
      }]
    },
    options: {
      scales: {
        x: {
          title: {
            display: true,
            text: 'Time'
          }
        },
        y: {
          title: {
            display: true,
            text: 'Y-axis Label'
          }
        }
      }
    }
  });
}

// Sample data for the graph (you can replace this with your data)
const x4Data = [1, 2, 3, 4, 5];
const y4Data = [10, 60, 15, 30, 25];

// Function to draw the graph using Chart.js
function drawGraph4() {
  const ctx = document.getElementById('myChart4').getContext('2d');
  const myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: x4Data,
      datasets: [{
        label: 'Glass Waste',
        data: y4Data,
        borderColor: 'rgb(75, 192, 192)',
        borderWidth: 2,
        fill: false,
      }]
    },
    options: {
      scales: {
        x: {
          title: {
            display: true,
            text: 'Time'
          }
        },
        y: {
          title: {
            display: true,
            text: 'Y-axis Label'
          }
        }
      }
    }
  });
}

// Sample data for the graph (you can replace this with your data)
const x5Data = [1, 2, 3, 4, 5];
const y5Data = [10, 60, 15, 30, 25];

// Function to draw the graph using Chart.js
function drawGraph5() {
  const ctx = document.getElementById('myChart5').getContext('2d');
  const myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: x5Data,
      datasets: [{
        label: 'Metal waste',
        data: y5Data,
        borderColor: 'rgb(75, 192, 192)',
        borderWidth: 2,
        fill: false,
      }]
    },
    options: {
      scales: {
        x: {
          title: {
            display: true,
            text: 'Time'
          }
        },
        y: {
          title: {
            display: true,
            text: 'Y-axis Label'
          }
        }
      }
    }
  });
}

// Sample data for the graph (you can replace this with your data)
const x6Data = [1, 2, 3, 4, 5];
const y6Data = [10, 60, 15, 30, 25];

// Function to draw the graph using Chart.js
function drawGraph6() {
  const ctx = document.getElementById('myChart6').getContext('2d');
  const myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: x6Data,
      datasets: [{
        label: 'Plastic Waste',
        data: y6Data,
        borderColor: 'rgb(75, 192, 192)',
        borderWidth: 2,
        fill: false,
      }]
    },
    options: {
      scales: {
        x: {
          title: {
            display: true,
            text: 'Time'
          }
        },
        y: {
          title: {
            display: true,
            text: 'Y-axis Label'
          }
        }
      }
    }
  });
}


// Call the drawGraph function to render the graph
drawGraph1();
drawGraph2();
drawGraph3();
drawGraph4();
drawGraph5();
drawGraph6();


// scroll back to top button 
// Get the button:
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