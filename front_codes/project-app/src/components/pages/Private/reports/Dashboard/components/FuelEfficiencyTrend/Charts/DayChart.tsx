import React, { FC } from 'react';
import { Line } from 'react-chartjs-2';

const data = {
  labels: ['08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18'],
  datasets: [
    {
      label: '하루 시간별대 연비',
      fill: false,
      lineTension: 0.1,
      backgroundColor: 'rgba(75,192,192,0.4)',
      borderColor: 'rgba(75,192,192,1)',
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: 'rgba(75,192,192,1)',
      pointBackgroundColor: '#fff',
      pointBorderWidth: 1,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: 'rgba(75,192,192,1)',
      pointHoverBorderColor: 'rgba(220,220,220,1)',
      pointHoverBorderWidth: 2,
      pointRadius: 1,
      pointHitRadius: 10,
      data: [33.1, 33.4, 31.3, 31.6, 33.2, 33.8, 32.7, 33.4, 31.7, 31.9, 32.3]
    }
  ]
};

const DayChart: FC = () => {
  return (
    <div>
      <Line data={data} />
    </div>
  )
}

export default DayChart;