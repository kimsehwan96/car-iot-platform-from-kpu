import React from 'react';
import { Button, Input, Form, Row, Col, Typography } from 'antd';

export default function Signup() {
    return (
    <>
    <Row justify="center">
        <Col style={{ marginTop: 100}}>
            <Typography.Title className="auth-title">Sign Up</Typography.Title>
        </Col>
    </Row>
      <Row justify="center">
        <Col style ={{ marginTop: 20 }}>
        <Form.Item
        name="name"
        label="Name"
        rules={[
          {
            type: 'name',
            message: 'The input is not valid Name!',
          },
          {
            required: true,
            message: 'Please input your Name',
          },
        ]}
      >
        <Input />
      </Form.Item>
        <Form.Item
        name="email"
        label="E-mail"
        rules={[
          {
            type: 'email',
            message: 'The input is not valid E-mail!',
          },
          {
            required: true,
            message: 'Please input your E-mail!',
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        name="password"
        label="Password"
        rules={[
          {
            required: true,
            message: 'Please input your password!',
          },
        ]}
        hasFeedback
      >
        <Input.Password />
      </Form.Item>

      <Form.Item
        name="confirm"
        label="Confirm Password"
        dependencies={['password']}
        hasFeedback
        rules={[
          {
            required: true,
            message: 'Please confirm your password!',
          },
          ({ getFieldValue }) => ({
            validator(rule, value) {
              if (!value || getFieldValue('password') === value) {
                return Promise.resolve();
              }
              return Promise.reject('The two passwords that you entered do not match!');
            },
          }),
        ]}
      >
        <Input.Password />
      </Form.Item>
        </Col>
    </Row>
    <Row justify ="center">
        <Form.Item>
            <Button type="primary" htmlType="submit" style ={{width: '30vh'}} >
                    인증 메일 받기
            </Button>
        </Form.Item>
    </Row>
    </>
    );
}
