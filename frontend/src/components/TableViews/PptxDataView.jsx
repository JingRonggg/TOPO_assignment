import React from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  Paper,
} from '@mui/material';

const PptxDataView = ({ data }) => {
  const [keyHighlights, revenueDistribution] = data;

  return (
    <Paper sx={{ overflow: 'auto' }}>
      <h2>Key Highlights</h2>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>ID</TableCell>
            <TableCell>Membership Sold</TableCell>
            <TableCell>Top Location</TableCell>
            <TableCell>Total Revenue</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {keyHighlights.map((highlight) => (
            <TableRow key={highlight.id}>
              <TableCell>{highlight.id}</TableCell>
              <TableCell>{highlight.membership_sold}</TableCell>
              <TableCell>{highlight.top_location}</TableCell>
              <TableCell>${highlight.total_revenue.toLocaleString()}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>

      <h2>Revenue Distribution</h2>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>ID</TableCell>
            <TableCell>Gym (%)</TableCell>
            <TableCell>Pool (%)</TableCell>
            <TableCell>Tennis Court (%)</TableCell>
            <TableCell>Personal Training (%)</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {revenueDistribution.map((distribution) => (
            <TableRow key={distribution.id}>
              <TableCell>{distribution.id}</TableCell>
              <TableCell>{distribution.gym}</TableCell>
              <TableCell>{distribution.pool}</TableCell>
              <TableCell>{distribution.tennis_court}</TableCell>
              <TableCell>{distribution.personal_training}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
  );
};

export default PptxDataView; 