import React, { useState } from 'react';
import { Layout } from 'antd';
import CardItem from './CardItem';
import MenuItem from '../component/MenuList';

const { Header, Footer, Sider, Content } = Layout;


export default function PageLayout() {
    const [collapsed, setCollapsed] = useState({collapsed: false});
    
    function onCollapse(collapsed) {
        setCollapsed(collapsed)
    }
    return (
        <>
        <Layout style={{ minHeight: '100vh'}}>
        <Sider collapsible collapsed={collapsed} onCollapse={onCollapse}>
            <MenuItem />
        </Sider>
        <Layout className="site-layout">
          <Header>
          </Header>
          <Content style ={{margin: '0 16px'}}>
            <CardItem />
          </Content>
          <Footer>Footer</Footer>
        </Layout>
      </Layout>
      </>
    )
}