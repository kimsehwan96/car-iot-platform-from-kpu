import React from 'react';
import { Link } from 'react-router-dom';
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
            <Link to="/dashboard"><DashboardFilled /><Text>Dashbord</Text></Link>
            </Menu.Item>
          <Menu.Item key="2" >
            <Link to="/pattern"><PieChartFilled /><Text>Pattern Analysis</Text></Link> 
          </Menu.Item>
        </Menu>
    </>
    )
}