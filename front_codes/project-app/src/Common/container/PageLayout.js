import React, { useState } from 'react';
import { Layout, PageHeader, Dropdown, Button, Menu } from 'antd';
import { Route } from 'react-router-dom';
import CardItem from '../../Dashbord/container/CardItem';
import MenuList from '../component/MenuList';
import PatternAnal from '../../PatternAnalysis/container/PatternAnal';
import { CarFilled, SettingOutlined} from '@ant-design/icons';

const { Sider, Content } = Layout;

const menu = (
  <Menu>
    <Menu.Item>
      로그 아웃
    </Menu.Item>
  </Menu>
)

const DropdownMenu = () => {
  return (
    <Dropdown key="more" overlay={menu}>
      <Button
        style={{
          border: 'none',
          padding: 0,
        }}
      >
        <SettingOutlined 
          style={{
            fontSize: 20,
            verticalAlign: 'top',
            backgroundColor:'#001529',
          }}
        />
      </Button>
    </Dropdown>
  );
};

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
            <DropdownMenu />
          }
        />
        <Layout className="site-layout">
          <Sider collapsible collapsed={collapsed} onCollapse={onCollapse}>
            <MenuList />
          </Sider>
          <Content style ={{margin: '0 16px'}}>
            <Route path="/dashboard"><CardItem /></Route>
            <Route path="/pattern"><PatternAnal/></Route>
          </Content>
        </Layout>
      </Layout>
      </>
    )
}