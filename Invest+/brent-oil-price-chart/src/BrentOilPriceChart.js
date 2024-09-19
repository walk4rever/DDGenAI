import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const data = [
  { year: '2014', price: 99 },
  { year: '2015', price: 52 },
  { year: '2016', price: 44 },
  { year: '2017', price: 54 },
  { year: '2018', price: 71 },
  { year: '2019', price: 64 },
  { year: '2020', price: 42 },
  { year: '2021', price: 71 },
  { year: '2022', price: 101 },
  { year: '2023', price: 82 },
  { year: '2024', price: 78 },
];

const BrentOilPriceChart = () => (
  <ResponsiveContainer width="100%" height={400}>
    <LineChart
      data={data}
      margin={{
        top: 5,
        right: 30,
        left: 20,
        bottom: 5,
      }}
    >
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="year" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="price" stroke="#8884d8" activeDot={{ r: 8 }} />
    </LineChart>
  </ResponsiveContainer>
);

export default BrentOilPriceChart;