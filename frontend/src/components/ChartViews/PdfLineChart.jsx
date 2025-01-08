import React from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const LineChartComponent = ({ data }) => {
  const sortedData = data.sort(
    (a, b) => a.year - b.year || ["Q1", "Q2", "Q3", "Q4"].indexOf(a.quarter) - ["Q1", "Q2", "Q3", "Q4"].indexOf(b.quarter)
  );

  const labels = sortedData.map((entry) => `${entry.quarter} ${entry.year}`);
  const revenues = sortedData.map((entry) => entry.revenue);
  const memberships = sortedData.map((entry) => entry.memberships_sold);

  const chartData = {
    labels,
    datasets: [
      {
        label: "Revenue ($)",
        data: revenues,
        borderColor: "rgba(75, 192, 192, 1)",
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        tension: 0.4,
      },
      {
        label: "Memberships Sold",
        data: memberships,
        borderColor: "rgba(255, 99, 132, 1)",
        backgroundColor: "rgba(255, 99, 132, 0.2)",
        tension: 0.4,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: "Quarterly Performance",
      },
    },
  };

  return <Line data={chartData} options={options} />;
};

export default LineChartComponent;
