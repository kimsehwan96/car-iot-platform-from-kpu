import React from 'react'
import { Radar } from '@ant-design/charts';
import { DataSet } from '@antv/data-set';
import { Typography } from 'antd';

const data = [
    {"item" : "급가속 횟수", 'userAverage': 13, 'kimsehwan': 24, 'leeyongbeom': 30},
    {"item" : "급제동 횟수", 'userAverage': 17, 'kimsehwan': 31,  'leeyongbeom': 40},
    {"item" : "급핸들링 횟수", 'userAverage': 21, 'kimsehwan': 38, 'leeyongbeom': 30},
]

const Score = () => {
    // const [data, setData] = useState([]);
    // useEffect(() => {
    //     asyncFetch();
    // }, []);
    // const asyncFetch = () => {
    //     fetch('https://gw.alipayobjects.com/os/bmw-prod/safe/${userId}')
    //         .then((response) => response.json())
    //         .then((json) => setData(json))
    //         .catch((error) => {
    //         console.log('fetch data failed', error);
    //     });
    // };
    const { DataView } = DataSet;
    const dv = new DataView().source(data);
    dv.transform({
        type: 'fold',
        fields: ['userAverage', 'kimsehwan', 'leeyongbeom'],
        key: 'user',
        value: 'score',
    });
    const config = {
        data: dv.rows,
        xField: 'item',
        yField: 'score',
        seriesField: 'user',
        meta: {
            score: {
                alias: '分数',
                min: 0,
                max: 40,
            },
        },
        xAxis: {
            line: null,
            tickLine: null,
            grid: {
                line: {
                    style: {
                        lineDash: null,
                    },
                },
            },
        },
        yAxis: {
            line: null,
            tickLine: null,
            grid: {
                line: {
                    type: 'line',
                    style: {
                        lineDash: null,
                    },
                },
            },
        },
        area: {},
        point: {},
    };
    return (
    <>
    <Radar {...config}/>
    <br/>
    <Typography.Text>[Total Score] 사용자 평균: 75점 김세환: 58점</Typography.Text>
    </>
    );
};
export default Score;