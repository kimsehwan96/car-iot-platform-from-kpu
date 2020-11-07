import React from 'react';
import { Line } from '@ant-design/charts';

const DrivingRecord = () => {
  const data = [
    {
      date: '20-10-04',
      km: 15,
    },
    {
      date: '20-10-05',
      km: 20,
    },
    {
      date: '20-10-06',
      km: 25,
    },
    {
      date: '20-10-08',
      km: 18,
    },
    {
      date: '20-10-09',
      km: 3,
    },
    {
      date: '120-10-10',
      km: 19,
    },
    {
      date: '20-10-11',
      km: 23,
    },
    {
      date: '20-10-12',
      km: 16,
    },
    {
      date: '20-10-13',
      km: 13,
    },
  ];
  const config = {
    appendPadding: 10,
    height: 300,
    data,
    xField: 'date',
    yField: 'km',
    point: {
      size: 5,
      shape: 'diamond',
    },
    label: {
      style: {
        fill: '#aaa',
      },
    },
  };
  return <Line {...config} />;
};
export default DrivingRecord;