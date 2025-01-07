import React, { useState, useEffect } from 'react';
import { Box, Tabs, Tab, CircularProgress, Alert } from '@mui/material';
import JsonDataView from './DataViews/JsonDataView';
import CsvDataView from './DataViews/CsvDataView';
import PdfDataView from './DataViews/PdfDataView';

const endpoints = {
  json: 'http://127.0.0.1:5000/api/data/json',
  csv: 'http://127.0.0.1:5000/api/data/csv',
  pdf: 'http://127.0.0.1:5000/api/data/pdf'
};

const Dashboard = () => {
  const [jsonData, setJsonData] = useState(null);
  const [csvData, setCsvData] = useState(null);
  const [pdfData, setPdfData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState(0);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [jsonResponse, csvResponse, pdfResponse] = await Promise.all([
          fetch(endpoints.json).then(res => res.json()),
          fetch(endpoints.csv).then(res => res.json()),
          fetch(endpoints.pdf).then(res => res.json())
        ]);

        setJsonData(jsonResponse);
        setCsvData(csvResponse);
        setPdfData(pdfResponse);
      } catch (err) {
        setError('Failed to fetch data');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <CircularProgress />;
  if (error) return <Alert severity="error">{error}</Alert>;

  return (
    <Box sx={{ width: '100%', padding: 3 }}>
      <Tabs value={activeTab} onChange={(_, newValue) => setActiveTab(newValue)} >
        <Tab label="Company Data (JSON)" />
        <Tab label="Member Activities (CSV)" />
        <Tab label="Quarterly Performance (PDF)" />
      </Tabs>

      {activeTab === 0 && <JsonDataView data={jsonData} />}
      {activeTab === 1 && <CsvDataView data={csvData} />}
      {activeTab === 2 && <PdfDataView data={pdfData} />}
    </Box>
  );
};

export default Dashboard;