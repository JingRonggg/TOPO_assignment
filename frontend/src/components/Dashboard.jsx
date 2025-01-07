import React, { useState, useEffect } from 'react';
import { 
  Box, 
  CircularProgress, 
  Alert, 
  Tabs, 
  Tab,
  TextField,
  MenuItem,
  Grid2
} from '@mui/material';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid2,
  Tooltip,
  Legend
} from 'recharts';
import JsonDataView from './DataViews/JsonDataView';
import CsvDataView from './DataViews/CsvDataView';
import PdfDataView from './DataViews/PdfDataView';

const Dashboard = () => {
  const [data, setData] = useState<any>(null);
  const [filteredData, setFilteredData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState(0);
  const [sortField, setSortField] = useState('');
  const [filterValue, setFilterValue] = useState('');

  useEffect(() => {
    fetchData();
  }, []);

  useEffect(() => {
    if (data) {
      applyFiltersAndSort();
    }
  }, [data, sortField, filterValue]);

  const fetchData = async () => {
    try {
      setLoading(true);
      const response = await fetch('http://localhost:5000/api/data');
      const result = await response.json();
      setData(result);
      setFilteredData(result);
    } catch (err) {
      setError('Failed to fetch data');
    } finally {
      setLoading(false);
    }
  };

  const applyFiltersAndSort = () => {
    let processed = [...data[activeTab]];

    // Apply filtering
    if (filterValue) {
      processed = processed.filter(item => 
        Object.values(item).some(val => 
          String(val).toLowerCase().includes(filterValue.toLowerCase())
        )
      );
    }

    // Apply sorting
    if (sortField) {
      processed.sort((a, b) => {
        if (a[sortField] < b[sortField]) return -1;
        if (a[sortField] > b[sortField]) return 1;
        return 0;
      });
    }

    setFilteredData(processed);
  };

  const getChartData = () => {
    if (!filteredData) return [];
    
    switch (activeTab) {
      case 0: // JSON data
        return filteredData.map((company) => ({
          name: company.name,
          revenue: company.revenue,
          employees: company.employees.length
        }));
      case 1: // CSV data
        return filteredData.slice(0, 10).map((activity) => ({
          name: activity.date,
          revenue: parseFloat(activity.revenue)
        }));
      case 2: // PDF data
        return filteredData.map((performance) => ({
          name: `${performance.year} Q${performance.quarter}`,
          revenue: performance.revenue,
          memberships: performance.memberships_sold
        }));
      default:
        return [];
    }
  };

  if (loading) return <CircularProgress />;
  if (error) return <Alert severity="error">{error}</Alert>;

  return (
    <Box sx={{ width: '100%', padding: 3 }}>
      <Tabs value={activeTab} onChange={(_, newValue) => setActiveTab(newValue)}>
        <Tab label="Company Data (JSON)" />
        <Tab label="Member Activities (CSV)" />
        <Tab label="Quarterly Performance (PDF)" />
      </Tabs>

      <Grid2 container spacing={3} sx={{ mt: 2 }}>
        <Grid2 item xs={12}>
          <Box sx={{ display: 'flex', gap: 2, mb: 2 }}>
            <TextField
              label="Filter"
              value={filterValue}
              onChange={(e) => setFilterValue(e.target.value)}
              size="small"
            />
            <TextField
              select
              label="Sort by"
              value={sortField}
              onChange={(e) => setSortField(e.target.value)}
              size="small"
            >
              {getAvailableSortFields().map((field) => (
                <MenuItem key={field} value={field}>
                  {field}
                </MenuItem>
              ))}
            </TextField>
          </Box>
        </Grid2>

        <Grid2 item xs={12}>
          <BarChart width={800} height={400} data={getChartData()}>
            <CartesianGrid2 strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="revenue" fill="#8884d8" />
            {activeTab === 0 && <Bar dataKey="employees" fill="#82ca9d" />}
            {activeTab === 2 && <Bar dataKey="memberships" fill="#82ca9d" />}
          </BarChart>
        </Grid2>

        <Grid2 item xs={12}>
          {activeTab === 0 && <JsonDataView data={filteredData} />}
          {activeTab === 1 && <CsvDataView data={filteredData} />}
          {activeTab === 2 && <PdfDataView data={filteredData} />}
        </Grid2>
      </Grid2>
    </Box>
  );
};

const getAvailableSortFields = () => {
  // Add relevant sort fields based on the data structure
  return ['name', 'revenue', 'date', 'year'];
};

export default Dashboard;