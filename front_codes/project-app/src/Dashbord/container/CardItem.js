import React, { useState } from 'react';
import { Card, Col, Row } from 'antd';
import DrivingRecord from '../component/DrivingRecord';
import MonthFuelEfficiency from '../component/MonthFuelEfficiency';
import DayFuelEfficiency from '../component/DayFuelEfficiency';
import EngineOil from '../component/EngineOil';

export default function CardItem() {
    const tabList = [
        { 
            key: 'Day', 
            tab: 'Day',
        }, 
        { 
            key: 'Month', 
            tab: 'Month', 
        },
    ];
    
    const contentList = {
        Day: <DayFuelEfficiency />,
        Month: <MonthFuelEfficiency />,
    };
    const [key, setKey] = useState('Day');

    function onTabChange(key) {
        setKey(key);
    }

    return (
    <div className="site-card-wrapper">
        <Row gutter={16}>
            <Col span={8}>
                <Card title="주행 기록(km)">
                    <DrivingRecord />
                </Card>
            </Col>
            <Col span={8}>
                <Card 
                title="연비(km/L)"
                tabList={tabList}
                activeTabKey={key}
                onTabChange={key => {
                    onTabChange(key);
                }}
                >  
                    {contentList[key]}
                </Card>
            </Col>
            <Col span = {8}>
                <Card title="엔진오일 잔여량(%)">
                    <EngineOil />
                </Card>
            </Col>
        </Row>
    </div>
    );
}

