import React from 'react';
import { Link } from 'react-router-dom';
import { Form, Input, Button, Row, Typography, Col } from 'antd'
import { UserOutlined, LockOutlined } from '@ant-design/icons';

const Login = () => {
    return (
    <>
      <Row justify="center" style={{ marginTop: 100 }}>
        <Col>
          <Typography.Title className="auth-title">WABD</Typography.Title>
        </Col>
      </Row>
      <Row justify="center">
        <Form
          name="normal_login"
          initialValues={{ remember: true }}
          style={{ width: 300, marginTop: 50 }}
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
      </Row>
    </>
    );
};

export default Login;