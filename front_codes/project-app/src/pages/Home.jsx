import React, { useState } from 'react'
import { Layout, Typography, Avatar, Menu } from 'antd';
import { CarFilled } from '@ant-design/icons'
import { Link, Route } from 'react-router-dom';
import { SidebarData } from '../components/SidebarData';
import Dashboard from '../pages/Dashboard';
import Pattern from '../pages/Pattern';
import Community from '../pages/Community';
import ContactUs from '../pages/ContactUs';
import Settings from '../components/Settings';

const { Header, Footer, Sider, Content } = Layout;
const { Title } = Typography;

export default function Home() {
    const [collapsed , setCollapsed] = useState(false);
    
    const onCollapse = () => setCollapsed(!collapsed);
    return (
    <div className="home">
        <Layout style={{ minHeight: '100vh' }}>
            <Header style={{padding:20}} >
                <Avatar style={{float:'left'}} icon={<CarFilled />} />
                <Title 
                    style={{color:'white', marginLeft: 40}} 
                    level={3}>
                        Web App for Beginner Drivers 
                        <Settings />
                </Title>
            </Header>
            <Layout>
                <Sider collapsible collapsed={collapsed} onCollapse={onCollapse}>
                    <Menu theme='dark' defaultSelectedKeys={['0']} mode="inline">
                        {SidebarData.map((item, index) => {
                            return (
                                <Menu.Item 
                                    key={index} 
                                    className={item.cName}
                                    icon={item.icon}
                                >
                                    <Link to={item.path}>
                                        {item.title}
                                    </Link>
                                </Menu.Item>
                            )
                        })}
                    </Menu>
                </Sider>         
                <Layout>
                    <Content style={{ padding: '0 50px' }}>
                        <Route path='/dashboard' component={Dashboard} />
                        <Route path='/pattern' component={Pattern} />
                        <Route path='/community' component={Community} />
                        <Route path='/contactus' component={ContactUs} />
                    </Content>
                    <Footer style={{ textAlign: 'center'}}>
                        Ant Design Created by kwHong
                    </Footer>
                </Layout>
            </Layout>
        </Layout>
    </div>
    )
}
