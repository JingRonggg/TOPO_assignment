import React from 'react';
import { 
  Card, 
  CardContent, 
  Typography, 
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow
} from '@mui/material';

const JsonDataView = ({ data }) => {
  return (
    <Grid container spacing={3}>
      {data.map((company) => (
        <Grid item xs={12} key={company.id}>
          <Card>
            <CardContent>
              <Typography variant="h5" gutterBottom>
                {company.name}
              </Typography>
              <Typography color="textSecondary">
                Industry: {company.industry}
              </Typography>
              <Typography color="textSecondary">
                Location: {company.location}
              </Typography>

              <Typography variant="h6" sx={{ mt: 2 }}>
                Employees
              </Typography>
              <Table size="small">
                <TableHead>
                  <TableRow>
                    <TableCell>Name</TableCell>
                    <TableCell>Role</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {company.employees.map((employee) => (
                    <TableRow key={employee.id}>
                      <TableCell>{employee.name}</TableCell>
                      <TableCell>{employee.role}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>

              <Typography variant="h6" sx={{ mt: 2 }}>
                Performance
              </Typography>
              <Table size="small">
                <TableHead>
                  <TableRow>
                    <TableCell>Quarter</TableCell>
                    <TableCell>Revenue</TableCell>
                    <TableCell>Profit Margin</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {company.performance.map((perf) => (
                    <TableRow key={perf.quarter}>
                      <TableCell>{perf.quarter}</TableCell>
                      <TableCell>${perf.revenue.toLocaleString()}</TableCell>
                      <TableCell>{perf.profit_margin}%</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </CardContent>
          </Card>
        </Grid>
      ))}
    </Grid>
  );
};

export default JsonDataView;