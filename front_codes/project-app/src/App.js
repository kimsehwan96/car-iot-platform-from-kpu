import React from 'react';
import 'antd/dist/antd.css';
import './App.css'
import PageLayout from './common/container/PageLayout';
import { Route } from 'react-router-dom';
import Login from './auth/container/Login';
import Signup from './auth/container/Signup';

function App() {  
  return (
    <>
      <Route path="/user" component={PageLayout} />
      <Route path="/login" component={Login} />
      <Route path="/signup" component={Signup} />
    </> 
  );
}

export default App;
