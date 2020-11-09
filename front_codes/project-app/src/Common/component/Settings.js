import React from 'react';
import { Link } from 'react-router-dom';
import { Dropdown, Button, Menu } from 'antd';
import { SettingOutlined } from '@ant-design/icons';

const menu = (
    <Menu>
        <Link to="/login">
            <Menu.Item style={{padding: 10}}>
                로그인
            </Menu.Item>
        </Link>
    </Menu>
  )

export default function Settings() {
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