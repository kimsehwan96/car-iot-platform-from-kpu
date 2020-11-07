import React from 'react';
import { Menu, Typography } from 'antd';
import {
    DashboardFilled,
    PieChartFilled,
} from '@ant-design/icons';

const { Text } = Typography;

export default function MenuList() {
    return(
    <>
        <div className="logo" />
        <Menu theme="dark" defaultSelectedKeys={['1']} mode='inline'>
          <Menu.Item key="1" >
            <DashboardFilled /><Text>Dashbord</Text>
          </Menu.Item>
          <Menu.Item key="2" >
            <PieChartFilled /><Text>Pattern Analysis</Text>
          </Menu.Item>
        </Menu>
    </>
    )
}