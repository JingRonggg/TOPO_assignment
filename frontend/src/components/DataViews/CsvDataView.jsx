import React from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  Paper
} from '@mui/material';

const CsvDataView = ({ data }) => {
  return (
    <Paper sx={{ overflow: 'auto' }}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Date</TableCell>
            <TableCell>Membership ID</TableCell>
            <TableCell>Type</TableCell>
            <TableCell>Activity</TableCell>
            <TableCell>Revenue</TableCell>
            <TableCell>Duration</TableCell>
            <TableCell>Location</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((activity) => (
            <TableRow key={activity.id}>
              <TableCell>{activity.date}</TableCell>
              <TableCell>{activity.membership_id}</TableCell>
              <TableCell>{activity.membership_type}</TableCell>
              <TableCell>{activity.activity}</TableCell>
              <TableCell>${activity.revenue}</TableCell>
              <TableCell>{activity.duration} mins</TableCell>
              <TableCell>{activity.location}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
  );
};

export default CsvDataView;