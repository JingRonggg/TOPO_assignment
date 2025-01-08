import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, LineElement, PointElement, LinearScale, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(LineElement, PointElement, LinearScale, Title, Tooltip, Legend);

const RevenueLineChart = ({ data }) => {
  // Prepare data for the line chart
  const labels = data.map(item => `${item.year} ${item.quarter}`);
  const revenueData = data.map(item => item.revenue);

  const chartData = {
    labels: labels,
    datasets: [
      {
        label: 'Revenue',
        data: revenueData,
        borderColor: '#36A2EB',
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        fill: true,
      },
    ],
  };

  return (
    <div>
      <h2>Revenue Over Time</h2>
      <Line data={chartData} />
    </div>
  );
};

export default RevenueLineChart;