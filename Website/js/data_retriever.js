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

      // Assign the daily_tracking feed data to dataDaily
      rawDataDaily = latestData.daily_tracking;
      dataDaily = rawDataDaily.split(" "); 
      dataDaily[1] = parseInt(dataDaily[1]);

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
    })
    .catch(error => {
      console.error("Error fetching data:", error);
    });
}

// Call the retrieveDataAndDisplay() function to fetch and process the data
retrieveDataAndDisplay();
