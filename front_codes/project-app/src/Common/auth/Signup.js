import React from 'react';
import { Button, Input, Form } from 'antd';

export default function Signup() {
    return (
    <>
        <Form.Item
            style={{ marginTop: 50, width: 300 }}
            name="name"
            rules={[
                {
                    required: true,
                    message: 'Please Input your E-mail',
                },
            ]}
        >
            <Input autoFocus addonAfter={EMAIL_SUFFIX} placeholder="" />
        </Form.Item>
        <Form.Item>
            <Button type="primary" htmlType="submit" style ={{width: '30vh'}} >
                인증 메일 받기
            </Button>
        </Form.Item>
    </>
    );
}

const EMAIL_SUFFIX = '@company.com'