import React from 'react';
import { Link } from 'react-router-dom';
import { Form, Input, Button } from 'antd'
import { UserOutlined, LockOutlined } from '@ant-design/icons';
/**
 * 회원가입 또는 로그인 폼을 보여줌
 */

const AuthForm = () => {
    return (
    <Form
      name="normal_login"
      initialValues={{ remember: true }}
      style={{ width: 300, marginTop: 50 }}
      onFinish={() => {}}
    >
      <Form.Item
        name="username"
        rules={[
          {
            required: true,
            message: 'Please input your Username!',
          },
        ]}
      >
        <Input 
        autoFocus
        prefix={<UserOutlined className="site-form-item-icon" />} 
        placeholder="Username" />
      </Form.Item>
      <Form.Item
        name="password"
        rules={[
          {
            required: true,
            message: 'Please input your Password!',
          },
        ]}
      >
        <Input
          prefix={<LockOutlined className="site-form-item-icon" />}
          type="password"
          placeholder="Password"
        />
      </Form.Item>
      <Form.Item>
        <Button type="primary" htmlType="submit" style={{ width: '100%' }}>
          Log in
        </Button>
        Or <Link to='signup'>register now!</Link>
      </Form.Item>
    </Form>
    );
};

export default AuthForm;