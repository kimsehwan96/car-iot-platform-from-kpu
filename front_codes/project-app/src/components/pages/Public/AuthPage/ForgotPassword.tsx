import React, { FC, FormEvent, useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../../../../store';
import { sendPasswordResetEmail, setError, setSuccess } from '../../../../store/actions/authActions';
import Message from '../../../UI/Message';
import { Container, Form, FormButton, FormContent, FormH1, FormInput, Formlabel, FormWrap, Icon } from './authElements';

const ForgotPassword: FC = () => {
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const dispatch = useDispatch();
  const { error, success } = useSelector((state: RootState) => state.auth);

  useEffect(() => {
    return () => {
      if(error) {
        dispatch(setError(''));
      }
      if(success) {
        dispatch(setSuccess(''));
      }
    }
  }, [error, success, dispatch]);

  const submitHandler = async (e: FormEvent) => {
    e.preventDefault();
    if (success) {
      dispatch(setSuccess(''));
    }
    if (error) {
      dispatch(setError(''));
    }
    setLoading(true);
    await dispatch(sendPasswordResetEmail(email, 'Email sent!'));
    setLoading(false);
  }

  return (
    <>
      <Container>
        <FormWrap>
          <Icon to='/'>Logo</Icon>
          <FormContent>
            <Form onSubmit={submitHandler}>
              {error && <Message type="danger" msg={error} />}
              {success && <Message type="success" msg={success} />}
              <FormH1>Send email for password reset</FormH1>
              <Formlabel htmlFor="for">Email</Formlabel>
              <FormInput 
                type="email" 
                aria-label="Email"
                value={email} 
                onChange={(e) => setEmail(e.currentTarget.value)} 
                required 
              />
              <FormButton 
                type="submit"
                disabled={loading}
              >
                  {loading ? 'Loading...' : 'Send Email'}
              </FormButton>
            </Form>
          </FormContent>
        </FormWrap>
      </Container> 
    </>
  )
}

export default ForgotPassword;
