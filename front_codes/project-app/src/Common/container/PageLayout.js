import React, { useState } from 'react';
import { Layout, PageHeader } from 'antd';
import { Route } from 'react-router-dom';
import CardItem from '../../dashbord/container/CardItem';
import MenuList from '../component/MenuList';
import PatternAnal from '../../pattern/container/PatternAnal';
import { CarFilled } from '@ant-design/icons';
import Settings from '../component/Settings';

const { Sider, Content } = Layout;

export default function PageLayout() {
    const [collapsed, setCollapsed] = useState(false);
    
    function onCollapse(collapsed) {setCollapsed(collapsed)}
    return (
        <>
        <Layout style={{ minHeight: '100vh'}}>
        <PageHeader
          className="site-page-header"
          title="WABD"
          subTitle="Web Application for Beginner Drivers"
          avatar= {<CarFilled />} 
          extra ={
            <Settings />
          }
        />
        <Layout className="site-layout">
          <Sider collapsible collapsed={collapsed} onCollapse={onCollapse}>
            <MenuList />
          </Sider>
          <Content style ={{margin: '0 16px'}}>
            <Route exact path="/user/dashboard" component ={CardItem} />
            <Route exact path="/user/pattern" component={PatternAnal} />
          </Content>
        </Layout>
      </Layout>
      </>
    )
}