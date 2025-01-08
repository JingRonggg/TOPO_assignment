import React from 'react';
import { Pie } from 'react-chartjs-2';

const RevenueDistributionChart = ({ data }) => {
  const revenueData = {
    labels: ['Gym', 'Pool', 'Tennis Court', 'Personal Training'],
    datasets: [
      {
        data: [
          data.gym,
          data.pool,
          data.tennis_court,
          data.personal_training
        ],
        backgroundColor: [
          '#FF6384',
          '#36A2EB',
          '#FFCE56',
          '#4BC0C0'
        ],
      },
    ],
  };

  return (
    <div>
      <Pie data={revenueData} />
    </div>
  );
};

export default RevenueDistributionChart; 