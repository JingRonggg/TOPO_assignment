const getChartData = (data) => {
  if (!data || !data[0].employees) {
    console.error("Invalid data structure: ", data);
    return { pieData: {} };
  }

  const employees = data[0].employees;
  const roleCounts = {};

  employees.forEach(employee => {
      const role = employee.role;
      roleCounts[role] = (roleCounts[role] || 0) + 1;
  });

  const roles = Object.keys(roleCounts);
  const counts = Object.values(roleCounts);

  const pieData = {
    labels: roles,
    datasets: [
      {
        data: counts,
        backgroundColor: [
          "#FF6384",
          "#36A2EB",
          "#FFCE56",
          "#4BC0C0",
          "#9966FF",
          "#FF9F40",
          "#FF6384",
          "#36A2EB",
          "#FFCE56",
          "#4BC0C0",
          "#9966FF",
          "#FF9F40",
          "#FF6384",
          "#36A2EB",
          "#FFCE56",
        ],
      },
    ],
  };

  return { pieData };
};

export default getChartData;