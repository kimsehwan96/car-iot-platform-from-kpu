import React, { FC, FormEvent, useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../../../../store';
import { setError, signup } from '../../../../store/actions/authActions';
import Message from '../../../UI/Message';
import { Container, Form, FormButton, FormContent, FormH1, FormInput, Formlabel, FormWrap, Icon } from './authElements';

const SignUp: FC = () => {
  const [firstName, setFirstName] = useState('');
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
    setLoading(true);
    dispatch(signup({ email, password, firstName }, () => setLoading(false)));
  }
  
  return (
    <>
     <Container>
        <FormWrap>
          <Icon to='/'>Logo</Icon>
          <FormContent>
            <Form onSubmit={submitHandler}>
              {error && <Message type="danger" msg={error} />}
              <FormH1>Sign up for your account</FormH1>
              <Formlabel htmlFor="for">FirstName</Formlabel>
              <FormInput 
                type="firstname" 
                aria-label="Firstname"
                value={firstName} 
                onChange={(e) => setFirstName(e.currentTarget.value)} 
                required 
              />
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
                  {loading ? 'Loading...' : 'Sign Up'}
              </FormButton>
            </Form>
          </FormContent>
        </FormWrap>
      </Container>
    </>
  )
}

export default SignUp;
