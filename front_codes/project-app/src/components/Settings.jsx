import React, { useState } from 'react'
import { SettingFilled } from '@ant-design/icons';
import { Dropdown, Menu, Button, Modal, Drawer } from 'antd';
import LoginForm from './LoginForm';
import SignupForm from './SignupForm';


export default function Settings() {
    // 로그인 세팅
    const [visible, setVisiable] = useState({
        onmodal : false,
        loading: false,
        ondrawer: false,
    });

    function showModal() {
        setVisiable({
            onmodal: true,
        });
    }

    function handleCancel() {
        setVisiable({
            onmodal: false,
        });
    }

    function handleOk() {
        setVisiable({ loading: true });
        setTimeout(() => {
            setVisiable({ onmodal: false, loading: false });
        }, 3000);
    }


    function showDrawer() {
        setVisiable({
            ondrawer: true,
        })
    }

    function closeDrawer() {
        setVisiable({
            onmodal: true,
            ondrawer: false,
        })
    }

    return (
    <>
        <Dropdown overlay={
            <Menu>
                <Menu.Item onClick={showModal}>로그인</Menu.Item>
            </Menu>
        }
        trigger={['click']}
        placement="bottomRight"
        >
            <Button style={{float: 'right'}} shape='circle' icon={<SettingFilled />} />
        </Dropdown>
        <Modal
            title="로그인 하기"
            visible={visible.onmodal}
            onCancel={handleCancel}   
            footer={[
                <Button key="back" onClick={handleCancel}>
                    나가기
                </Button>,
                <Button key="signup" onClick={showDrawer}> 
                    가입하기
                </Button>,
                <Button key="login" type="primary" loading={visible.loading} onClick={handleOk}>
                    로그인
                </Button>,
            ]}
        >
            <LoginForm />
        </Modal>
            <Drawer
            title="회원가입"
            width={720}
            visible={visible.ondrawer}
            onClose={closeDrawer}
            bodyStyle={{paddingBottom: 80}}
            footer ={
                <div 
                    style={{textAlign: 'right'}}
                >
                    <Button onClick={closeDrawer} style={{ marginRight: 8}}>
                        취소
                    </Button>
                    <Button onClick={closeDrawer} type="primary">
                        제출
                    </Button>
                </div>
            }
        >
            <SignupForm />
        </Drawer>
    </>
    )
}
