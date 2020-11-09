import React, { useState } from 'react';
import { Layout, PageHeader } from 'antd';
import { Route } from 'react-router-dom';
import CardItem from '../../dashbord/container/CardItem';
import MenuList from '../component/MenuList';
import PatternAnal from '../../pattern/container/PatternAnal';
import { CarFilled } from '@ant-design/icons';

import Settings from '../component/Settings';
import AuthForm from '../auth/AuthForm';
import Signup from '../auth/Signup';

const { Sider, Content } = Layout;

export default function PageLayout() {
    const [collapsed, setCollapsed] = useState(false);
    
    function onCollapse(collapsed) {
        setCollapsed(collapsed)
    }
    return (
        <>
        <Layout style={{ minHeight: '100vh'}}>
        <PageHeader
          className="site-page-header"
          title="초보운전자를 위한 웹 어플리케이션"
          subTitle="운전 실력 향상 앱"
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
            <Route path="/dashboard" component ={CardItem} />
            <Route path="/pattern" component={PatternAnal} />
            <Route path="/login" component={AuthForm} />
            <Route path="/signup" component={Signup} />
          </Content>
        </Layout>
      </Layout>
      </>
    )
}