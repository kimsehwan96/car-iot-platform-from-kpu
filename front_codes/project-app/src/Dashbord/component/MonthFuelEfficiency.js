import React from 'react';
import { Column } from '@ant-design/charts';

const MonthFuelEfficiency = () => {
  const data = [
    {
      month: '5월',
      fe: 21.4,
    },
    {
      month: '6월',
      fe: 21.8,
    },
    {
      month: '7월',
      fe: 20.9,
    },
    {
      month: '8월',
      fe: 22.1,
    },
    {
      month: '9월',
      fe: 21.7,
    },
  ];
  const config = {
    appendPadding: 10,
    height: 260,
    data,
    xField: 'month',
    yField: 'fe',
  };
  return <Column {...config} />;
};

export default MonthFuelEfficiency;
