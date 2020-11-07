import React from 'react';
import { Gauge } from '@ant-design/charts';

const DayFuelEfficiency = () => {
    const config = {
        appendPadding: 10,
        height: 260,
        percent: 0.48,
        range: {
            ticks: [0, 0.2, 0.4, 0.75, 1],
            color: ['#9EDCA6', '#BFE8C3', '#EFF3DE', '#FFE9B8', '#FFDE94'],
        },
        indicator: {
            pointer: {
                style: {
                    stroke: '#D0D0D0',
                },
            },
            pin: {
                style: {
                    stroke: '#D0D0D0',
                },
            },
        },
        axis: {
            label: {
                formatter: function formatter(v) {
                    return Number(v) * 40;
                },
            },
            subTickLine: {
                count: 3,
            },
        },
        statistic: {
            content: {
                formatter: function formatter(_ref) {
                    const { percent } = _ref;
                    return 'F.E: '.concat(percent * 40 , 'km/L');
                },
            },
            style: {
                fontSize: 30,
            },
        },
    };
    return <Gauge {...config} />;
};

export default DayFuelEfficiency;