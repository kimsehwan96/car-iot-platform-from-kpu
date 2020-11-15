import React from 'react'
import { SettingFilled } from '@ant-design/icons';
import { Dropdown, Menu, Button } from 'antd';
import LoginModal from './LoginModal';



export default function Settings() {
    function openLoginModal() {
        return <LoginModal />
    }
    return (
        <Dropdown overlay={
            <Menu>
                <Menu.Item onClick={openLoginModal}>로그인</Menu.Item>
            </Menu>
        }
        trigger={['click']}
        placement="bottomRight"
        >
            <Button style={{float: 'right'}} shape='circle' icon={<SettingFilled />} />
        </Dropdown>
    )
}
