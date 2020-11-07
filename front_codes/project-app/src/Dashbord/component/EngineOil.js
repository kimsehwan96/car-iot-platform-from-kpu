import React from 'react';
import { Liquid } from '@ant-design/charts';

export default function EngineOil() {
    const config = {
        appendPadding: 10,
        height: 300,
        percent: 0.78,
        statistic: {
            content: {
                style: {
                    fontSize: 60,
                    fill: 'black'
                },
            },
        },
    };
    return <Liquid {...config} />;
};
