import React, { useState } from 'react'
import { Form, Row, Col, Input, Button } from 'antd'
import UserPool from '../libs/UserPool';


export default function SignupForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');


  const onSubmit = e => {
    e.preventDefault();

    UserPool.signUp(email, password, [], null, (err, data) => {
      if(err) console.error(err);
      console.log(data);
    });
  };

    return (
    <Form >
      <Row gutter={24}>
        <Col span={12}>
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
              <Input onChange={e => setEmail(e.target.value)}/>
            </Form.Item>

            <Form.Item
              name="password"
              label="Password"
              rules={[
                {
                  required: true,
                  message: 'Please input your passsword!',
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
                    if(!value || getFieldValue('password') === value) {
                      return Promise.resolve();
                    }

                    return Promise.reject('The two password that you entered do not match!');
                  },
                }),
              ]}
              >
                <Input.Password onChange={e => setPassword(e.target.value)}/>
              </Form.Item>
        </Col>
      </Row>
          <Button onClick={onSubmit} type="primary" htmlType="submit">Resister</Button>
    </Form>
    )
}
