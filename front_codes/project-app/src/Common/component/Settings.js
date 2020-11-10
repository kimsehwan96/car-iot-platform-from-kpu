import React from 'react';
import { Dropdown, Button, Menu } from 'antd';
import { SettingOutlined } from '@ant-design/icons';


export default function Settings() {
    return (
      <Dropdown key="more" overlay ={
          <Menu>
              <Menu.Item>로그 아웃</Menu.Item>
          </Menu>
      }
      trigger={['click']}
      placement="bottomRight"
    >
        <Button shape="circle" icon={<SettingOutlined />} />
      </Dropdown>
    );
  };