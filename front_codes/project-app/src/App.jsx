import React from 'react'
import 'antd/dist/antd.css';
import { BrowserRouter as Router , Switch, Route } from 'react-router-dom';
import Home from './pages/Home';


function App() {


  return (
      <Router>
        <Switch>
          <Route path='/' component={Home} />
        </Switch>
      </Router>
  )
}

export default App;

