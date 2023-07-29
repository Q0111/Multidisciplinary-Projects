// Mã JavaScript để vẽ biểu đồ Bar Chart và Pie Chart sẽ được thêm ở đây
document.addEventListener("DOMContentLoaded", function () {
    // Dữ liệu và cấu hình cho biểu đồ Bar Chart và Pie Chart
    var barChartData1 = {
        labels: ['Organic', 'Paper', 'Glass', 'Metal', 'Plastic'],
        datasets: [{
            label: "Total Quantity",
            data: [10, 20, 15, 25, 90],
            backgroundColor: ['orange', 'red', 'blue', 'green', 'yellow']
        }]
    };

    var pieChartData1 = {
        labels: ['Organic', 'Paper', 'Glass', 'Metal', 'Plastic'],
        datasets: [{
            data: [25, 30, 15, 10, 20],
            backgroundColor: ['orange', 'red', 'blue', 'green', 'yellow']
        }]
    };

    // Tạo các biểu đồ Bar Chart và Pie Chart
    var barChart1 = new Chart(document.getElementById('barChart1'), {
        type: 'bar',
        data: barChartData1
    });

    var pieChart1 = new Chart(document.getElementById('pieChart1'), {
        type: 'pie',
        data: pieChartData1
    });

});