import React from 'react'
import Score from '../libs/score';
import { Row, Col, Card } from 'antd';
import UserRank from '../libs/UserRank';

export default function Pattern() {
    return (
        <div>
            <Row gutter={24} style={{marginTop:30}}>
                <Col span={6}>
                    <Card title="item1">
                        000 
                    </Card>
                </Col>
                <Col span={6}>
                    <Card title="item2">
                        000 
                    </Card>
                </Col>
                <Col span={6}>
                    <Card title="item3">
                        000
                    </Card>
                </Col>
                <Col span={6}>
                    <Card title="item4">
                        000
                    </Card>
                </Col>
                <Col span={12 } style={{marginTop: 30, textAlign:"center"}}>
                    <Card title="당신의 점수는?">
                        <Score/>
                    </Card> 
                </Col>
                <Col span={12} style={{marginTop: 30, textAlign:"center"}}>
                    <Card title="사용자 랭킹">
                        <UserRank />
                    </Card>
                </Col>
            </Row>
        </div>
    )
}
