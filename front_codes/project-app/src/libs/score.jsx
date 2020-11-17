import React from 'react'
import { Radar } from '@ant-design/charts';
import { DataSet } from '@antv/data-set';

const data = [
    {"item" : "급가속 횟수", 'userAverage': 13, 'kimsehwan': 24 },
    {"item" : "급정거 횟수", 'userAverage': 17, 'kimsehwan': 31 },
    {"item" : "급핸들링 횟수", 'userAverage': 21, 'kimsehwan': 38 },
    {"item" : "욕설 횟수", 'userAverage': 14, 'kimsehwan': 18 },
    {"item" : "경적 횟수", 'userAverage': 21, 'kimsehwan': 24},
]

const Score = () => {
    // const [data, setData] = useState([]);
    // useEffect(() => {
    //     asyncFetch();
    // }, []);
    // const asyncFetch = () => {
    //     fetch('https://gw.alipayobjects.com/os/bmw-prod/bda695a8-cd9f-4b78-a423-3d6d547c10c3.json')
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
        fields: ['userAverage', 'kimsehwan'],
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
        // 开启面积
        area: {},
        // 开启辅助点
        point: {},
    };
    return <Radar {...config}/>;
};
export default Score;