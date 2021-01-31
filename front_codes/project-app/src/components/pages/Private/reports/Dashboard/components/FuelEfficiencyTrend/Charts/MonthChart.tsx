import React, { FC } from 'react';
import { Line } from 'react-chartjs-2';

const data = {
  labels: ['Jan', 'Fed', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
  datasets: [
    {
      label: '월별 연비 추이',
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
      data: [34.1, 32.4, 32.3, 32.6, 31.2, 34.8, 35.7, 34.4, 32.7, 33.9, 31.3, 33.7 ],
    }
  ]
};

const MonthChart: FC = () => {
  return (
    <div>
      <Line data={data} />
    </div>
  )
}

export default MonthChart;