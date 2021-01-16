import React, { FC, FormEvent, useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../../../../store';
import { setError, signin } from '../../../../store/actions/authActions';
import { Container, Form, FormButton, FormContent, FormH1, FormInput, Formlabel, FormWrap, Icon, TextButton } from './authElements'
import Message from '../../../UI/Message';
import { Link } from 'react-router-dom';

const SignIn: FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const dispatch = useDispatch();
  const { error } = useSelector((state: RootState) => state.auth);

  useEffect(() => {
    return () => {
      if(error) {
        dispatch(setError(''));
      }
    }
  }, [error, dispatch]);
 
  const submitHandler = (e: FormEvent) => {
    e.preventDefault();
    if (error) {
      dispatch(setError(''));
    }
    setLoading(true);
    dispatch(signin({ email, password }, () => setLoading(false)));
  }

  return (
    <>
      <Container>
        <FormWrap>
          <Icon to='/'>Logo</Icon>
          <FormContent>
            <Form onSubmit={submitHandler}>
              {error && <Message type="danger" msg={error} />}
              <FormH1>Sign in to your account</FormH1>
              <Formlabel htmlFor="for">Email</Formlabel>
              <FormInput 
                type="email" 
                aria-label="Email"
                value={email} 
                onChange={(e) => setEmail(e.currentTarget.value)} 
                required 
              />
              <Formlabel htmlFor="for">Password</Formlabel>
              <FormInput 
                type="password" 
                aria-label="password"
                value={password}
                onChange={(e) => setPassword(e.currentTarget.value)}
                required 
              />
              <FormButton 
                type="submit"
                disabled={loading}
              >
                  {loading ? 'Loading...' : 'Continue'}
              </FormButton>
              <Link to="/forgot-password">
                <TextButton>Forgot password?</TextButton>
              </Link>
            </Form>
          </FormContent>
        </FormWrap>
      </Container>
    </>
  )
}

export default SignIn;
