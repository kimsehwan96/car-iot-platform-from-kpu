import React, { FC, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import firebase from './firebase/config';
import { RootState } from './store';
import { getUserById, setLoading, setNeedVerification } from './store/actions/authActions';
import Loader from './components/UI/Loader';
import { BrowserRouter, Switch } from 'react-router-dom';
import PublicRoute from './components/auth/PublicRoute';
import HomePage from './components/pages/Public/HomePage/HomePage';
import SignIn from './components/pages/Public/AuthPage/SignIn';
import ForgotPassword from './components/pages/Public/AuthPage/ForgotPassword';
import Signup from './components/pages/Public/AuthPage/SignUp';
import PrivateRoute from './components/auth/PrivateRoute';
import UserApp from './components/pages/Private/UserApp';

import './App.css';


const App: FC = () => {
  const dispatch = useDispatch();
  const { loading } = useSelector((state: RootState) => state.auth);

  //Check if user exists
  useEffect(() => {
    dispatch(setLoading(true));
    const unsubscribe = firebase.auth().onAuthStateChanged(async (user) => {
      if (user) {
        dispatch(setLoading(true));
        await dispatch(getUserById(user.uid)); 
        if(!user.emailVerified) {
          dispatch(setNeedVerification());
        }
      }
      dispatch(setLoading(false));
    });

    return() => {
      unsubscribe();
    };
  }, [dispatch])

  if(loading){
    return <Loader />;
  }

  return (
    <BrowserRouter>
      <Switch>
        <PublicRoute path="/" component={HomePage} exact/>
        <PublicRoute path="/signup" component={Signup} exact/>
        <PublicRoute path="/signin" component={SignIn} exact/>
        <PublicRoute path="/forgot-password" component={ForgotPassword} exact/>
        <PrivateRoute path="/app" component={UserApp} />
      </Switch>
    </BrowserRouter>
  );

}

export default App;
