import React, { useState } from 'react';
import { Layout } from 'antd';
import { Route } from 'react-router-dom';
import CardItem from '../../Dashbord/container/CardItem';
import MenuList from '../component/MenuList';
import PatternAnal from '../../PatternAnalysis/container/PatternAnal';

const { Header, Sider, Content } = Layout;


export default function PageLayout() {
    const [collapsed, setCollapsed] = useState({collapsed: false});
    
    function onCollapse(collapsed) {
        setCollapsed(collapsed)
    }
    return (
        <>
        <Layout style={{ minHeight: '100vh'}}>
        <Sider collapsible collapsed={collapsed} onCollapse={onCollapse}>
            <MenuList />
        </Sider>
        <Layout className="site-layout">
          <Header>
          </Header>
          <Content style ={{margin: '0 16px'}}>
            <Route path="/dashboard"><CardItem /></Route>
            <Route path="/pattern"><PatternAnal/></Route>
          </Content>
        </Layout>
      </Layout>
      </>
    )
}