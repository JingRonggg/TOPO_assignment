import React, { useState } from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  TableSortLabel,
  Paper
} from '@mui/material';

const PdfDataView = ({ data }) => {
  const [sortConfig, setSortConfig] = useState({ key: null, direction: 'asc' });

  const sortedData = React.useMemo(() => {
    if (sortConfig.key) {
      return [...data].sort((a, b) => {
        const aValue = a[sortConfig.key];
        const bValue = b[sortConfig.key];

        if (aValue < bValue) {
          return sortConfig.direction === 'asc' ? -1 : 1;
        }
        if (aValue > bValue) {
          return sortConfig.direction === 'asc' ? 1 : -1;
        }
        return 0;
      });
    }
    return data;
  }, [data, sortConfig]);

  const handleSort = (key) => {
    setSortConfig((prev) => {
      const isAsc = prev.key === key && prev.direction === 'asc';
      return { key, direction: isAsc ? 'desc' : 'asc' };
    });
  };

  return (
    <Paper sx={{ overflow: 'auto' }}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>
              <TableSortLabel
                active={sortConfig.key === 'year'}
                direction={sortConfig.key === 'year' ? sortConfig.direction : 'asc'}
                onClick={() => handleSort('year')}
              >
                Year
              </TableSortLabel>
            </TableCell>
            <TableCell>Quarter</TableCell>
            <TableCell>
              <TableSortLabel
                active={sortConfig.key === 'revenue'}
                direction={sortConfig.key === 'revenue' ? sortConfig.direction : 'asc'}
                onClick={() => handleSort('revenue')}
              >
                Revenue
              </TableSortLabel>
            </TableCell>
            <TableCell>
              <TableSortLabel
                active={sortConfig.key === 'memberships_sold'}
                direction={sortConfig.key === 'memberships_sold' ? sortConfig.direction : 'asc'}
                onClick={() => handleSort('memberships_sold')}
              >
                Memberships Sold
              </TableSortLabel>
            </TableCell>
            <TableCell>
              <TableSortLabel
                active={sortConfig.key === 'duration'}
                direction={sortConfig.key === 'duration' ? sortConfig.direction : 'asc'}
                onClick={() => handleSort('duration')}
              >
                Duration (Minutes)
              </TableSortLabel>
            </TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {sortedData.map((performance) => (
            <TableRow key={performance.id}>
              <TableCell>{performance.year}</TableCell>
              <TableCell>{performance.quarter}</TableCell>
              <TableCell>${performance.revenue}</TableCell>
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
