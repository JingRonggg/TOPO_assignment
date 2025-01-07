import React from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  Paper
} from '@mui/material';

const PdfDataView = ({ data }) => {
  return (
    <Paper sx={{ overflow: 'auto' }}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Year</TableCell>
            <TableCell>Quarter</TableCell>
            <TableCell>Revenue</TableCell>
            <TableCell>Memberships Sold</TableCell>
            <TableCell>Duration</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((performance) => (
            <TableRow key={performance.id}>
              <TableCell>{performance.year}</TableCell>
              <TableCell>{performance.quarter}</TableCell>
              <TableCell>${performance.revenue.toLocaleString()}</TableCell>
              <TableCell>{performance.memberships_sold}</TableCell>
              <TableCell>{performance.duration}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
  );
};

export default PdfDataView;