import React, { useState } from 'react'
import { Button, Form, Input } from 'antd';
import { UserOutlined, LockOutlined } from '@ant-design/icons'
import { CognitoUser, AuthenticationDetails } from 'amazon-cognito-identity-js';
import UserPool from '../libs/UserPool';

export default function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  
  const onSubmit = e => {
    e.preventDefault();

    const user = new CognitoUser({
      Username: email,
      Pool: UserPool,
    });

    const atuhDetails = new AuthenticationDetails({
      Username: email,
      Password: password,
    });

    user.authenticateUser(atuhDetails, {
      onSuccess: data => {
        console.log('onSuccess: ', data);
      },

      onFailure: err => {
        console.log('onFailure: ', err);
      },

      newPasswordRequired: data => {
        console.log('newPasswordRequired: ', data);
      }
    });
  };

    return (
        <Form
      name="normal_login"
      className="login-form"
      initialValues={{ remember: true }}
      onFinish={() => {}}
    >
      <Form.Item
        name="email"
        rules={[{ required: true, message: 'Please input your email!' }]}
      >
        <Input onChange={e => setEmail(e.target.value)} prefix={<UserOutlined className="site-form-item-icon" />} placeholder="E-mail" />
      </Form.Item>
      <Form.Item
        name="password"
        rules={[{ required: true, message: 'Please input your Password!' }]}
      >
        <Input
          prefix={<LockOutlined className="site-form-item-icon" />}
          type="password"
          placeholder="Password"
          onChange={e => setPassword(e.target.value)}
        />
      </Form.Item>
      <Button type="primary" onClick={onSubmit}>로그인</Button>
    </Form>
    )
}
